# Domain 5 — Governance, Safety & Risk Management

**Weight:** 14% (source: official exam guide v1.0, effective July 2026 — `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`)
**Objectives covered:** Implement guardrails and safety controls · Identify risks, limitations, and failure modes of LLM systems · Apply human-in-the-loop validation strategies · Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP) · Address ethical AI considerations (bias, fairness, transparency)

---

## 5.1 Guardrail Layering

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Implement guardrails and safety controls |
| The four layers | Input validation (pre-call) · output filtering (post-call) · scoped permissions · human approval on consequential actions |
| Discriminator | Does the design have independent layers, or one control carrying everything |
| Cost dimension | Layers are cheap; each is a small deterministic check. A single tuned classifier costs more to build and covers less |
| Failure mode | One layer is bypassed by exactly the case it was not written for, and nothing behind it catches the miss |

### Layer Coverage — Single Control vs Defense in Depth

The four layers fail independently, so an incident must clear all four; adding a fifth flavour of one layer adds nothing.

| Situation | Answer | Why |
|---|---|---|
| Output classifier is the only safety control on a customer-facing assistant | Add pre-call input validation, tool scoping, and a human gate on consequential actions | A single layer is a single point of failure; the other three catch different classes |
| Team proposes replacing four simple checks with one fine-tuned safety model | Reject | Correlated coverage from one mechanism; independence is what the layering buys |
| Assistant already has input validation, output filtering, and scoped tools, and can issue refunds up to $10,000 unattended | Add the human-approval layer on the consequential action | The irreversible action is the uncovered layer |
| A low-consequence internal drafting tool with no external output and no tools | Input validation and output schema checks are sufficient | Layers are matched to consequence; permission scoping and human gates have nothing to cover here |

### Exam scenario: a support assistant's only safety control is an output classifier, and it has begun taking actions users did not request

- ✅ Add independent layers — validate and delimit untrusted input before the call, scope the tool set to what the task requires, and gate consequential actions on human approval
- ❌ Retrain the output classifier on the new failure examples — **HALF-MOVE**: improves the one layer that already exists, leaves the design at one layer, and does nothing about the action path
- ❌ Add detailed logging and alerting on unexpected tool calls so the team can respond quickly — **WRONG-AXIS**: detection, not prevention; the question is how to stop the action, and a log records it after it happened

### ❌ Misconception
"We have a strong safety classifier, so the system is guarded." — One layer is a single point of failure; guardrails work because input validation, output filtering, permission scoping, and human approval fail independently.

---

## 5.2 Least Privilege in Tool Scoping

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Implement guardrails and safety controls |
| Rule | Least privilege means **removing** an unneeded capability, not logging or confirming its use |
| Source alignment | Consistent with the answer logic in the official guide's sample items |
| Strongest form | Move the model out of the action path entirely — it emits a recommendation, a separate service holding the credential executes |
| Stakeholder answer | "The assistant cannot do X. It proposes; the existing system decides." |

### Capability Handling — Remove vs Monitor

If the task does not require the capability, delete it; monitoring, confirming, and rate-limiting all presuppose the capability still exists.

| Situation | Answer | Why |
|---|---|---|
| Agent has a write/delete tool it has never legitimately needed | Remove the tool | The failure class disappears rather than being mitigated |
| Agent needs the capability sometimes, and misuse is consequential | Model emits a structured request; a separate service holding the credential validates and executes | Privilege stays outside the model while the capability remains available |
| Agent needs the capability routinely, misuse is low-consequence and reversible | Keep the tool, add logging | Removal would break the task; the consequence does not justify a gate |
| Proposal: keep the dangerous tool and log every invocation | Reject as the primary control | Logging is detection; the action still executes |

### Exam scenario: an agent has a `delete_records` tool it does not need for its stated task

- ✅ Remove `delete_records` from the agent's tool definitions
- ❌ Keep the tool and log every invocation for audit — **WRONG-AXIS**: right vocabulary (audit, least privilege), wrong mechanism; the deletion still happens
- ❌ Keep the tool but require a confirmation step before it executes — **HALF-MOVE**: a partial version of the right answer that leaves the capability in place and depends on whoever confirms

### ❌ Misconception
"Least privilege is satisfied by auditing privileged actions." — It is satisfied by not granting the privilege; auditing describes what a granted privilege did.

---

## 5.3 Compliance Boundary Enforcement

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Ensure compliance with regulations |
| Rule | A required control cannot depend on the model behaving correctly; probabilistic behaviour does not produce a guarantee |
| Pattern | Classify → de-identify or tokenise before the call → re-associate locally → audit the crossing |
| Timing test | A control that acts after the request is assembled is too late; the boundary crossing has already occurred |
| Three failed conversions | High measured accuracy · documented residual risk · a larger model — none turns a tendency into a guarantee |

### Control Placement — Pre-Boundary Mechanism vs Model Instruction

Ask when the control fires relative to the data crossing the boundary; only a control that fires first can prevent the crossing.

| Situation | Answer | Why |
|---|---|---|
| Regulated identifiers must never reach the inference endpoint | De-identify or tokenise in the pipeline before the call | Deterministic, fires before transmission, independent of model behaviour |
| Same requirement, proposal is a system-prompt instruction to ignore identifiers | Reject | Evaluated after the identifiers are already in the request, and depends on compliance |
| Same requirement, proposal is nightly redaction of stored logs | Reject as the control | Fixes the record, not the transmission |
| Requirement is a strong preference rather than an absolute (e.g., preferred tone in redactions) | A prompt instruction is appropriate | The requirement is a tendency, so a tendency-shaped mechanism fits |

### Exam scenario: a healthcare client requires that patient identifiers never leave their network, and the team proposes adding "do not repeat or store patient identifiers" to the system prompt

- ✅ De-identify the record in the pipeline before the API call, hold the re-identification map inside the network, and re-associate locally on return
- ❌ Keep the prompt instruction and support it with evaluation showing 99.4% compliance — **OVERSPEC** in appearance, insufficient in fact: a measured rate is still a tendency, and the requirement is absolute
- ❌ Sign a data processing agreement with the provider and document the residual risk — **ARCHITECTED**: reads as the mature governance answer, allocates liability, and does not stop the data crossing

### ❌ Misconception
"If we instruct the model clearly enough and measure high compliance, the requirement is met." — The instruction acts after the data has crossed the boundary, and a measured rate is a tendency; absolute requirements need a deterministic control that fires first.

---

## 5.4 Regulatory Regimes — What Each Forces Into the Design

### Core Facts

| Regime | Scope | What it forces into the architecture |
|---|---|---|
| **GDPR** | Personal data of people in the EU | Lawful purpose declared before collection and processing confined to it · data minimisation in the payload · erasure on request reaching every derived store · processing-location constraints on which endpoint may be used · ability to account for automated decisions affecting a person |
| **HIPAA** | US protected health information | De-identify before PHI leaves the covered boundary, or bring the processor inside it under agreement · minimum necessary excerpt · audit trails over PHI access · re-identification key stays inside the boundary |
| **FedRAMP** | Cloud services used by US federal agencies | Processing must run in an authorised environment at the appropriate impact level · constrains deployment topology and which models are available · continuous monitoring and documented control implementation |

### Which Constraint Binds — Payload Shape vs Deployment Environment

GDPR and HIPAA mostly constrain *what is in the request*; FedRAMP mostly constrains *where the request may be processed*.

| Situation | Answer | Why |
|---|---|---|
| EU customer records feeding a support assistant | Minimise fields to what the task needs, declare purpose, ensure the endpoint region is permitted, enumerate every store for erasure | GDPR binds payload contents, purpose, and location |
| Clinical narratives drafted by an assistant | Strip direct identifiers before the call, send the narrative, reattach locally, log access | HIPAA binds what leaves the covered boundary |
| Federal agency deployment where the preferred model is not in an authorised environment | The model is unavailable for that data; route through an authorised environment or keep the data out | FedRAMP is a boundary and procurement fact, not a configuration setting |
| A GDPR erasure request arrives for a customer whose support tickets seeded an evaluation dataset and a vector index | Deletion must reach the logs, the evaluation dataset, and the index | Derived data is still that person's data |

### Exam scenario: a federal agency wants the highest-capability model available, which is not offered in an authorised environment

- ✅ Deploy on an authorised environment using an available model, and state the capability trade-off explicitly to the sponsor
- ❌ Use the preferred model and add compensating controls plus enhanced monitoring — **ARCHITECTED**: sounds rigorous, but authorisation is a property of the environment and no control added on top confers it
- ❌ Use the preferred model for non-sensitive requests and the authorised one for sensitive requests, routed by a model-side classification of the input — **HALF-MOVE**: the routing decision itself is probabilistic, so regulated data reaches the unauthorised environment whenever the classifier is wrong

### ❌ Misconception
"FedRAMP is a configuration setting we can enable." — It is an authorisation status of the environment; if the environment is not authorised, no configuration or added control makes the deployment compliant.

---

## 5.5 Retention & Auditability

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Ensure compliance with regulations |
| Rule | Retention requires a stated purpose and a bounded duration; storage is a decision that creates obligations |
| Audit record contents | What was sent · when · under what purpose · which model and prompt version · what returned · outcome |
| Property required | Immutability — an audit trail that can be edited is not evidence |
| Cost dimension | Every retained interaction is erasure scope, breach surface, and discoverable material |

### Storage Posture — Justified Retention vs Default Retention

Storage is justified by a named purpose with a duration attached; "it might be useful later" is not a purpose.

| Situation | Answer | Why |
|---|---|---|
| Team proposes retaining all requests and responses indefinitely for future evaluation work | Reject; define purpose and duration, and de-identify what is kept | Indefinite retention of regulated content creates open-ended obligations |
| Incident investigation needs recent traffic | Bounded window (e.g., 30 days), de-identified, purpose-coded | Purpose and duration both stated |
| Regulator may ask why a specific decision was made | Retain the decision trace — inputs used, versions, thresholds, outcome — under its own policy | Explainability needs the trace, which is narrower and longer-lived than raw logs |
| Auditability requirement met by application logs the operations team can edit | Reject | Mutable records are not evidence of a boundary crossing |

### Exam scenario: a team wants to retain every model interaction indefinitely "so we can build evaluation datasets later"

- ✅ Define a bounded retention window with a stated purpose, de-identify what is retained, and keep a separate longer-lived decision trace for auditability
- ❌ Retain everything but restrict access to the team via role-based permissions — **HALF-MOVE**: access control is real and does not reduce retention scope, erasure obligations, or breach surface
- ❌ Retain everything and run a redaction job over the store on a schedule — **REPAIR**: fixes the record downstream of a decision that could have been prevented by not storing the field in the first place

### ❌ Misconception
"Keeping everything is the cautious choice — you can always delete later." — Retention creates obligations from the moment of storage; purpose and duration have to justify keeping the data, and erasure has to reach every store that holds it.

---

## 5.6 LLM Failure-Mode Diagnosis

### Core Facts

| Symptom | Root cause | Not the cause |
|---|---|---|
| Confidently wrong immediately after a content refresh | Retrieval / indexing | The model's reasoning ability |
| No memory of something said two turns earlier, short conversation | Application not resending history | Context window exceeded |
| Quality degrades only on long inputs, on mid-document content | Uneven attention across position | Input length alone |
| Behaviour changed with no code deployment | Model version drift | Prompt regression |
| Every step passes its own test, end-to-end accuracy is far lower | Compounding across steps (0.96^10 ≈ 66%) | Any single step |
| Agent took an unrequested action after processing an external document | Indirect prompt injection | User error |

### Diagnosis Discipline — Symptom Signature vs Model Capability

Reason from when and where the failure appears; a capability explanation that ignores the timing is almost always wrong.

| Situation | Answer | Why |
|---|---|---|
| RAG answers turned confident and wrong the day the corpus was reindexed | Investigate chunking, embedding version, and index freshness | Timing points at the pipeline change, not the model |
| Ten-step agent at 96% per step delivering ~66% end-to-end | Insert deterministic validation checkpoints mid-chain | Interrupts compounding; a better model shifts each step marginally |
| Same prompt, same code, different behaviour this week | Check the pinned model version and run the regression set | Drift is the only explanation consistent with no code change |
| Risk register ranking: a rare irreversible action vs a frequent recoverable one | Rank the irreversible one higher | Professional-tier risk ranking weights consequence and reversibility, not frequency alone |

### Exam scenario: a RAG assistant begins producing confident, specific, incorrect answers the week after the document corpus was refreshed

- ✅ Investigate the retrieval and indexing pipeline — chunk boundaries, embedding model version, stale or duplicated index entries
- ❌ Upgrade to a higher-capability model to reduce hallucination — **DISCARD**: replaces a working component to solve a fault that lives elsewhere, and the timing evidence points away from the model
- ❌ Add "only answer from the provided context" to the system prompt — **REPAIR**: patches the output of a pipeline that is supplying wrong context; the model is already faithfully reporting what it was given

### ❌ Misconception
"Confidently wrong output means the model is hallucinating." — When the fault is in retrieval, the model is faithfully reporting incorrect context; diagnose from the symptom's timing before touching the model.

---

## 5.7 Prompt Injection & Untrusted Retrieved Content

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Identify risks, limitations, and failure modes of LLM systems |
| Mechanism | Instructions and data share one channel, so any text the model reads can attempt to act as an instruction |
| Indirect injection sources | Retrieved web pages, PDFs, support tickets, code comments, calendar invites, email bodies |
| Structural control | Remove privilege from the model; validate the requested action, not the text requesting it |
| Failure mode | The agent performs a legitimate-looking tool call that no user asked for |

### Control Type — Privilege Removal vs Content Filtering

Filtering catches phrasings that were anticipated; removing privilege means a successful injection has nothing to reach.

| Situation | Answer | Why |
|---|---|---|
| Agent summarises third-party documents and holds a tool that can send email | Remove the send capability, or require human approval on send | Injection has no privileged action to hijack |
| Same agent, proposal is a filter for known injection phrasings | Keep as a layer, reject as the control | Novel phrasings pass; the capability is untouched |
| Retrieved content must be included in context | Wrap it in a delimited block the system prompt declares as data, and never let eligibility or authorisation decisions depend on its contents | Reduces the attack surface without pretending the channel is separated |
| Agent processes only internally authored, access-controlled content and holds no external tools | Delimiting plus input validation is proportionate | Lower exposure; a human gate would cost more than the risk |

### Exam scenario: an agent that summarises customer-submitted documents sent emails that no user requested

- ✅ Remove the email-send capability from the agent and route outbound messages through a service that requires human approval
- ❌ Add a filter that detects and strips instruction-like text from submitted documents — **HALF-MOVE**: a useful layer that catches known phrasings and leaves the privileged capability in place
- ❌ Strengthen the system prompt to state that content inside documents is never to be followed as an instruction — **REPAIR**: a prompt-level tendency defending an architectural exposure

### ❌ Misconception
"Prompt injection is a content problem we can filter." — It follows from instructions and data sharing one channel; the durable control is that the model holds no privilege worth hijacking.

---

## 5.8 Human-in-the-Loop Routing

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Apply human-in-the-loop validation strategies |
| Routing variables | Confidence **and** consequence, together |
| Absolute rule | Above a consequence threshold, route to a human regardless of confidence |
| Valid confidence signals | Independent verifier agreement · retrieval score · schema validation result · calibrated classifier · business rules (amount, tenure, jurisdiction) |
| Invalid confidence signal | The model's own statement of how sure it is |
| Cost dimension | Review percentage × volume × minutes per review = headcount. State it |
| Failure mode | Automation bias — a reviewer shown a fluent conclusion without its evidence approves it |

### Review Allocation — Two-Variable Routing vs Blanket or Sampled Review

Route on confidence and consequence together; a strategy that names only one variable, or none, is incomplete by construction.

| Situation | Answer | Why |
|---|---|---|
| High volume, high accuracy, mixed consequence | Auto-approve high-confidence low-consequence; route the rest by threshold; always route high-consequence | Allocates a scarce resource to where being wrong is expensive |
| Any irreversible or externally visible action (denial, payment, message to a customer) | Human, regardless of confidence | The human supplies accountability, not additional accuracy |
| Monitoring whether the auto-approved threshold is still correct | Continuous small sample of the auto-approved stream, audited on a schedule | Measures the unsupervised path; distinct from routing by sample |
| Volume figure is stated in the scenario and 100% review is proposed | Reject | The volume figure is there to make blanket review unstaffable |
| Genuinely low-volume, uniformly high-consequence work (e.g., a handful of regulatory filings per month) | Human review of every item is correct | Blanket review is wrong because of scale, not on principle |

### Exam scenario: 40,000 documents a day, extraction accuracy 94%, errors on financial figures are costly and errors on formatting are not

- ✅ Route by consequence and confidence — auto-approve high-confidence non-financial extractions, send every financial-figure extraction and every low-confidence item to review, and continuously sample the auto-approved stream
- ❌ Review 100% of outputs initially and relax as confidence grows — **ARCHITECTED**: reads as the prudent staged answer, has no exit criterion or capacity plan, and 40,000 daily reviews is the reason the volume was stated
- ❌ Review a random 10% sample of all outputs — **WRONG-AXIS**: uniform sampling encounters costly cases in proportion to their rarity; sampling is a calibration mechanism for the automated path, not a routing policy

### ❌ Misconception
"Start by reviewing everything and dial it back once we trust it." — Without an exit criterion, a measurement, and staffing to match, blanket review is a policy that never relaxes; route by confidence and consequence from the start.

---

## 5.9 Independent Verification of Confident Output

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Identify risks, limitations, and failure modes of LLM systems |
| Rule | Catching confident-but-wrong output requires verification independent of the model |
| Not independent | Asking the same model to double-check · a second call with the same context · a self-reported confidence score |
| Weakly independent | A second model — correlated training data means two models can agree and both be wrong |
| Independent | Deterministic validation against structured source data, a database lookup, schema and constraint checks, existence checks on every citation |
| Where it pays most | Immediately after steps whose errors are cheap to detect and expensive to propagate |

### Verification Source — Outside the Model vs Inside It

Independence means the check can fail when the model succeeds and succeed when the model fails; a check drawing on the same process cannot.

| Situation | Answer | Why |
|---|---|---|
| Extracted figures must match the source document | Deterministic comparison against the structured source | Fails independently of the generation |
| Cited policy clauses must exist | Look each citation up in the policy database before release | Existence is checkable without the model |
| Free-text summary quality with no ground truth available | A second-model or rubric-based check, with its correlation limits stated | Best available; not a guarantee, and say so |
| Team proposes a self-critique pass to catch hallucination | Accept as a quality improvement, reject as the control | Reduces the rate; shares the failure mode |

### Exam scenario: a system produces fluent, confident, occasionally fabricated figures, and the team proposes a second pass in which the model reviews its own output

- ✅ Validate every emitted figure deterministically against the structured source record and block release on mismatch
- ❌ Add a self-critique pass where the model checks its own output for errors — **WRONG-AXIS**: right vocabulary (verification), wrong source; the check is produced by the process that produced the error
- ❌ Use a second, different model as a checker and accept output when both agree — **HALF-MOVE**: more independent than a self-check and still correlated; two models can agree and both be wrong

### ❌ Misconception
"Have the model check its own work before returning it." — A self-check shares the failure mode of the generation; verification has to come from outside the model, and two models agreeing is agreement, not evidence.

---

## 5.10 Bias & Fairness Measurement

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Address ethical AI considerations (bias, fairness, transparency) |
| Rule | Aggregate accuracy is a weighted average that hides subgroup failure |
| Evaluation design | Stratified by the subgroups the organisation is accountable for, with adequate N **per group** rather than population-proportional |
| Proxy variables | Postal code, school name, employment gaps, name morphology, phrasing register |
| Conflict | Equal selection rate, equal false-negative rate, and equal calibration cannot generally hold together when base rates differ |
| Stakeholder answer | Declare which harm is being controlled, and therefore which fairness definition is in force |
| Failure mode | Fairness treated as a property measured once, rather than a measurement that moves with the population |

### Bias Control — Disaggregated Measurement vs Attribute Removal

Measure by subgroup; removing the protected attribute leaves the proxy signal intact and removes the ability to detect the disparity.

| Situation | Answer | Why |
|---|---|---|
| 91% aggregate accuracy, complaints concentrated in one group | Disaggregate the metric by subgroup on a stratified set | The aggregate cannot show what is being reported |
| Proposal to drop the protected attribute from the input | Reject as the fairness control | Proxies carry the signal, and measurement becomes impossible |
| Small subgroup, population-proportional evaluation sample | Rebalance to equal N per group | Proportional sampling gives the least power where the risk is highest |
| Two fairness metrics cannot both be satisfied | Choose by which harm is being controlled and record the rationale | The conflict is mathematical; the resolution is a stated decision |
| Fairness measured once at launch and signed off | Recompute on live traffic on a schedule | The applicant or customer population moves |

### Exam scenario: a screening system reports 91% overall accuracy and is generating complaints from one demographic group

- ✅ Rebuild the evaluation set stratified with equal N per group, report accuracy and false-negative rate per subgroup, and set the threshold against the worst-performing group
- ❌ Remove the demographic attribute from the model input — **DISCARD**: discards the field rather than adjusting the measurement, leaves proxy signal untouched, and eliminates the ability to detect disparity
- ❌ Raise the overall accuracy target and retrain until it is met — **WRONG-AXIS**: optimises the aggregate that was concealing the problem

### ❌ Misconception
"Remove the protected attribute and the system can't be biased." — Proxy variables carry the same signal, and removing the attribute destroys the measurement that would have detected the disparity.

---

## 5.11 Transparency — Disclosure vs Explainability

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Address ethical AI considerations (bias, fairness, transparency) |
| Two distinct meanings | **Disclosure** — the affected person knows AI was involved and how to reach a human. **Explainability** — a specific decision can be accounted for afterwards |
| Explainability artefact | A logged, reconstructable trace: inputs used, evidence retrieved, prompt and model version, score, threshold in force, rule applied, human decision |
| Not an explainability artefact | A model-generated rationale, which is plausible text about the decision rather than a record of what produced it |
| Contestability | A consequential decision needs a route to challenge it and reach a human, designed in rather than retrofitted |
| Cost dimension | The trace is cheap at write time and expensive to reconstruct after the fact |

### Accounting for a Decision — Logged Trace vs Generated Rationale

An auditor needs what actually determined the outcome; a rationale generated after the fact is subject to the same failure modes as the decision.

| Situation | Answer | Why |
|---|---|---|
| Regulator asks why a specific applicant was declined | Produce the stored trace — fields used, versions, score, threshold, rule | Reconstructs the actual decision path |
| Team proposes attaching a model-written explanation to each decision | Useful for the end user, not the audit record | A generated rationale can be confidently wrong about its own causes |
| Requirement is that people know they are interacting with an AI system | Disclosure at the point of interaction, plus a stated route to a human | Disclosure, not explainability — different requirement, different mechanism |
| Consequential automated decision with no challenge path | Add a contestation route with a queue and a status field | Cheap at design time; expensive after the first complaint |

### Exam scenario: an auditor asks the team to explain why a particular automated decision was made

- ✅ Retrieve the stored decision trace — the input fields used, the retrieved evidence, prompt and model versions, the score, and the threshold in force
- ❌ Re-run the case and ask the model to explain its reasoning — **REPAIR**: reconstructs an explanation after the fact from a non-deterministic process, rather than having recorded what happened
- ❌ Provide the system prompt and the model card as the account of the decision — **HALF-MOVE**: documents the system's general behaviour and says nothing about this decision

### ❌ Misconception
"The model can explain its own decisions, so the system is explainable." — A generated rationale is plausible text produced after the fact; explainability is a logged trace of the inputs, versions, and thresholds that actually determined the outcome.
