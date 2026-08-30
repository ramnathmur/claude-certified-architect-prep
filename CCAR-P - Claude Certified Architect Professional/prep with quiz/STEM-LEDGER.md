# CCAR-P Stem Ledger — v1

**Built:** 2026-08-29 · **Seeded with 48 stems before Paper 1 exists.**

This is the only ledger that can be populated before a paper ships, and it is the reason to build it
first. Every generated stem is compared against every row here before the paper is allowed to ship.

## What is stored, and why it is not the prose

Each row carries a **token signature** — the stem's content words, lowercased, deduplicated, stop
words removed — and an excerpt long enough to identify the row by eye. The signature is what the
duplicate check actually consumes; the full prose lives in the source file named in each row and is
not copied here.

## Sources

| Source | Rows | Why it is in the ledger |
|---|---|---|
| `mock-exams/CCAR-P_ExternalMock-1/2/3_v1.html` | 45 | Community-authored, permanently outside the `MockTest-N` sequence, and Ram may sit them. A generated stem that collides with one teaches nothing new |
| `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf` §8 | 3 | Ram has read these. They are the style reference, so a stem that reproduces one is measuring recall of the guide |
| Generated CCAR-P papers | 0 | None exist yet. Every shipped paper appends its 63 stems here |

## Threshold, calibrated rather than inherited

Foundations uses **0.40** Jaccard. That threshold was set on stems with a 51.5-word median. CCAR-P
stems are capped at 45 words and the official samples run 29 to 37, so the same threshold behaves
differently on a smaller token set — this was flagged as unresolved in the engine audit and is
resolved here by measuring it.

All 1128 pairs among the 48 seeded stems were scored.

| Statistic | Value |
|---|---|
| Pairs scored | 1128 |
| Maximum | **0.480** |
| Second highest | **0.207** |
| 99th percentile | 0.138 |
| 95th percentile | 0.077 |
| Median | 0.000 |
| Pairs ≥ 0.40 | 1 |
| Pairs ≥ 0.30 | 1 |
| Pairs ≥ 0.25 | 1 |

| Score | Pair |
|---|---|
| 0.480 | XM1-11 ~ OFF-2 |
| 0.207 | XM1-15 ~ OFF-1 |
| 0.190 | XM1-14 ~ XM2-15 |
| 0.182 | XM1-12 ~ XM2-10 |
| 0.182 | XM2-07 ~ XM3-09 |
| 0.182 | XM2-13 ~ XM3-07 |
| 0.182 | XM3-07 ~ XM3-09 |
| 0.167 | XM2-03 ~ XM3-02 |

### The top pair is a real duplicate, and that is the useful result

`XM1-11 ~ OFF-2` scores **0.480**. The next pair scores **0.207**. That is not a tail
of a distribution, it is a different population of size one: ExternalMock-1's question 11 and the
official guide's sample 2 are the same item — a repeated large static prefix with a short varying
suffix, answered by ordering static content first and enabling prompt caching. The community set
derived that item from the guide.

Two things follow. The community mocks are not fully independent of the guide, which is worth knowing
before treating them as extra practice. And the metric separates a genuine duplicate from unrelated
items by a factor of 2.3 on this corpus, which is what a usable gate needs.

### Ruling: 0.30 for CCAR-P, not the Foundations 0.40

Independent pairs top out at **0.207**; the one known duplicate sits at **0.480**.
Any threshold in that gap separates the two classes cleanly. 0.30 is chosen rather than 0.35 or 0.25
because it sits above every independent pair with ~45% headroom and still fires well below the
Foundations gate.

A 0.40 gate would have passed nothing here except the known duplicate, and on Foundations it passed a
paper carrying 20 of 60 stems above 0.30 with one at 0.833. The threshold was too loose there and
would be looser here, because a CCAR-P stem capped at 45 words carries fewer tokens than the
Foundations 51.5-word median and so has less room to accumulate overlap.

**Caveat on the sample.** The 45 ExternalMock stems average 15.3 words against the official samples'
29 to 38, so their median token set is 9 against the official 20 to 25. Small sets make unrelated
pairs score lower, which means the 0.207 independent maximum is likely an underestimate of what
full-length generated stems will produce. Recalibrate after Paper 1 adds 63 stems written to the
28-to-45-word band, and expect the independent maximum to rise. If it rises past 0.25, move the
threshold to 0.35 rather than accepting false positives.

## Ledger

| id | src | domain | words | excerpt | token signature |
|---|---|---|---|---|---|
| `XM1-01` | ExternalMock-1 | D1 | 18 | A retailer wants Claude to answer product questions… | `000 answer architecture catalog changes claude daily document fits product questions retailer wants` |
| `XM1-02` | ExternalMock-1 | D3 | 17 | After a re-index, your retrieval system returns semantically… | `after comes commercially first index investigation products retrieval returns semantically similar system wrong` |
| `XM1-03` | ExternalMock-1 | D3 | 21 | An agent used by 300 employees exposes 45… | `300 across agent architectural degrading eight employees exposes quality response selection systems tools used` |
| `XM1-04` | ExternalMock-1 | D4 | 12 | Which evaluation design best fits a summarization feature… | `best design evaluation feature fits quality subjective summarization` |
| `XM1-05` | ExternalMock-1 | D4 | 12 | Before a prompt change reaches all users, what… | `all before change disciplined prompt reaches sequence users` |
| `XM1-06` | ExternalMock-1 | D5 | 22 | A hospital system requires that protected health information… | `both clinicians design free health hospital information model need never protected provider reach requires satisfies search system text while` |
| `XM1-07` | ExternalMock-1 | D5 | 10 | Which is the correct application of human-in-the-loop review… | `application correct human loop review scale` |
| `XM1-08` | ExternalMock-1 | D6 | 24 | An executive sponsor demands a single accuracy number… | `accuracy architect competent demands document executive number performance present sharply single sponsor system type varies` |
| `XM1-09` | ExternalMock-1 | D5 | 16 | Your design must satisfy GDPR for EU customer… | `architecture customer data design directly gdpr most requirement satisfy shapes` |
| `XM1-10` | ExternalMock-1 | D1 | 17 | Which is the correct reason to prefer a… | `agent correct document intake prefer process reason workflow` |
| `XM1-11` | ExternalMock-1 | D2 | 18 | An application sends an identical 12,000-token policy preamble… | `000 addresses application both cost every identical latency optimization policy preamble request sends token` |
| `XM1-12` | ExternalMock-1 | D6 | 11 | What belongs in an architecture decision record for… | `architecture belongs claude decision record system` |
| `XM1-13` | ExternalMock-1 | D4 | 15 | Observability for a production agent should capture which… | `agent capture diagnosable following incidents make observability production` |
| `XM1-14` | ExternalMock-1 | D7 | 19 | A partner team wants to adopt your Claude… | `adopt adoption claude code durable handoff makes one partner rather setup team time wants` |
| `XM1-15` | ExternalMock-1 | D3 | 16 | Which change best reduces risk in an agent… | `agent best both change modify production read records reduces risk` |
| `XM2-01` | ExternalMock-2 | D3 | 15 | A client requires that inference run inside their… | `account aws client determine inference inside requires run` |
| `XM2-02` | ExternalMock-2 | D3 | 16 | An enterprise standardised on Google Cloud wants identity… | `audit cloud controls enterprise existing follows google handled identity standardised wants` |
| `XM2-03` | ExternalMock-2 | D3 | 15 | What is the main architectural benefit of routing… | `all architectural benefit internal main model one routing service through traffic` |
| `XM2-04` | ExternalMock-2 | D1 | 12 | Two designs both satisfy the requirement; one is… | `both decides designs materially one requirement satisfy simpler two` |
| `XM2-05` | ExternalMock-2 | D1 | 15 | A required compliance control depends on the model… | `behaving compliance control correct correctly depends judgment model required` |
| `XM2-06` | ExternalMock-2 | D1 | 15 | Where should the boundary of automation be drawn… | `affecting automation boundary customer decisions drawn makes solution` |
| `XM2-07` | ExternalMock-2 | D4 | 9 | What must exist before a solution is declared… | `before declared exist production ready solution` |
| `XM2-08` | ExternalMock-2 | D4 | 14 | An evaluation set contains only cases the system… | `already cases contains effect evaluation handles set system` |
| `XM2-09` | ExternalMock-2 | D5 | 14 | How should a request to log every prompt… | `audit every handled log prompt request response` |
| `XM2-10` | ExternalMock-2 | D5 | 12 | Who is accountable when an automated Claude workflow… | `accountable automated claude decision harmful produces workflow` |
| `XM2-11` | ExternalMock-2 | D6 | 18 | A sponsor asks for one number that shows… | `asks number one response right shows solution sponsor whether working` |
| `XM2-12` | ExternalMock-2 | D6 | 17 | A ten-user pilot is about to expand to… | `architect expand first pilot raise ten thousand two user users` |
| `XM2-13` | ExternalMock-2 | D2 | 13 | How should a model be chosen for a… | `chosen containing distinct model several solution tasks` |
| `XM2-14` | ExternalMock-2 | D2 | 11 | How should the context window be treated in… | `context design production treated window` |
| `XM2-15` | ExternalMock-2 | D7 | 15 | An organization wants consistent Claude Code practice across… | `across claude code consistent dozens durable most organization practice repositories wants` |
| `XM3-01` | ExternalMock-3 | D3 | 19 | A client will not accept a solution whose… | `accept auditor behavior cannot client constrain explained solution` |
| `XM3-02` | ExternalMock-3 | D3 | 17 | What is the main risk of building directly… | `abstraction against building cloud directly main model risk service single` |
| `XM3-03` | ExternalMock-3 | D3 | 15 | A solution must serve users in two regions… | `data different follows regions residency rules serve solution two users` |
| `XM3-04` | ExternalMock-3 | D1 | 16 | A requirement is stated as make it as… | `accurate architect make possible requirement stated` |
| `XM3-05` | ExternalMock-3 | D1 | 17 | Two components each work correctly but the system… | `boundary components correctly each fails intermittently suggest system two work` |
| `XM3-06` | ExternalMock-3 | D5 | 13 | A design proposes storing every model interaction indefinitely.… | `architect design every indefinitely interaction model proposes raise storing` |
| `XM3-07` | ExternalMock-3 | D5 | 14 | How should a solution handle the case where… | `case confident handle model solution wrong` |
| `XM3-08` | ExternalMock-3 | D4 | 14 | An evaluation shows 94% accuracy. What else must… | `accuracy actionable before else evaluation known shows` |
| `XM3-09` | ExternalMock-3 | D4 | 13 | What should happen when a model version is… | `beneath happen model production solution updated version` |
| `XM3-10` | ExternalMock-3 | D6 | 17 | A stakeholder asks why the solution cannot simply… | `answer asks automated cannot fully most simply solution stakeholder useful` |
| `XM3-11` | ExternalMock-3 | D6 | 14 | What should be handed over with a solution… | `first handed solution survives year` |
| `XM3-12` | ExternalMock-3 | D2 | 18 | A team reports the solution has become worse,… | `become deployed explanation has likely most nothing reports solution team worse` |
| `XM3-13` | ExternalMock-3 | D2 | 9 | How should prompts that determine production behavior be… | `behavior determine managed production prompts` |
| `XM3-14` | ExternalMock-3 | D7 | 18 | An organization asks how to measure whether Claude… | `asks claude code cost license measure measured organization whether worth` |
| `XM3-15` | ExternalMock-3 | D7 | 17 | What most often blocks a team from getting… | `blocks claude code codebase existing getting good most often results team` |
| `OFF-1` | Official guide v1.0 §8 | D3 | 38 | A team exposes a customer-support agent that can… | `accounts agent applying best change customer delete draft ever exposes issue least need principles privilege read reduces refunds replies risk staff support team tickets user` |
| `OFF-2` | Official guide v1.0 §8 | D2 | 33 | An application sends the same 8,000-token system prompt… | `000 addresses application both concerns cost directly document every followed latency message most optimization policy prompt request sends short system token user varying` |
| `OFF-3` | Official guide v1.0 §8 | D4 | 29 | A RAG system suddenly returns confident but incorrect… | `after answers confident document first incorrect investigate latency likely model most place rag refresh returns suddenly system unchanged version while` |


### Paper 1 — appended 2026-08-30

| id | src | domain | words | excerpt | token signature |
|---|---|---|---|---|---|
| `P1-01` | Paper 1 | D1 | 39 | A subscription business decides 60,000 refund-eligibility cases monthly… | `000 adjudicators against billing business case cases correctness cost decides decision disputed eligibility fits ledger licensed minutes monthly records refund reserves scoping shows statute structured subscription target unit within` |
| `P1-02` | Paper 1 | D1 | 36 | A quoting service prices each request along one… | `000 200 along auditor current daily each execution fits fixed identical inputs internal one partway path paths pattern prices pricing pulling quoting request requests requires service take through` |
| `P1-03` | Paper 1 | D1 | 39 | A surveillance coordinator delegates to four subagents; timeouts… | `apply completion compliance coordinator coverage delegates desk filing fixes four grades lines one overlaps product recur regulatory retried select severity subagents surveillance timeouts two unexamined while whole` |
| `P1-04` | Paper 1 | D1 | 35 | An intake service passes 500,000 documents monthly to… | `000 500 billing cannot change documents extraction file fits formats garbage header identifiable intake model monthly output parse passes percent reaches roughly service system two` |
| `P1-05` | Paper 1 | D1 | 39 | A review team scores 40 grant proposals in… | `against awards cap checked decided decomposition director every fits fixed funding get grant justification later never one pool proposal proposals requires review running scores sitting team thinner` |
| `P1-06` | Paper 1 | D1 | 33 | A checkout confirmation service commits to a 2.5-second… | `chains change checkout commits confirmation current data design independently loyalty made p95 pull second sequence service six steps tier two updates weekly` |
| `P1-07` | Paper 1 | D1 | 35 | A due-diligence brief must cover four independent lines… | `architecture brief budgeted commits cover delivering desk diligence due each fifteen fits four independent inquiry lines minutes request set spend token tool within` |
| `P1-08` | Paper 1 | D1 | 38 | Subagents search several sources each and return prose… | `agent audit cannot change claim claims each every findings fits five one out prose regulated rests return returned search several sources subagents synthesis though timed trace trail two` |
| `P1-09` | Paper 1 | D1 | 41 | A contract-review model flags risky clauses; whether a… | `actual archival caused change clauses confirmed contract discards dispute each ends false fits flag flags known later lawyers mark marks model positive review risky term tool whether years` |
| `P1-10` | Paper 1 | D1 | 37 | A stakeholder funds a model that auto-fills the… | `000 auto charges closing contract credits each eighteen fills fits funds hours inspection jobs model monthly need paperwork per percent repeat response second service stakeholder two visit` |
| `P1-11` | Paper 1 | D1 | 31 | A regulator requires a root-cause report within five… | `300 arrive cause days design each fits five incident incidents names next production queried query regulator report requires root roughly system within yearly` |
| `P1-12` | Paper 1 | D2 | 38 | A nightly job assigns one of twelve exception… | `assigns breaches ceiling change code codes completion cost each exactly exception fitting four job make million monthly nightly now one overruns records run shipment team twelve window` |
| `P1-13` | Paper 1 | D2 | 40 | A regulated advisory assistant runs thirty-turn sessions, with… | `advice adviser advisory assistant both boundary call carry crossing defined disclosure every fixed handoff hold initiate itself licensed placements regulated requests response runs select sessions thirty turn two` |
| `P1-14` | Paper 1 | D2 | 36 | An extraction service returns records in a documented… | `already change cost deviate documented downstream explicit extraction fail five fix instructions materially nightly parser per percent raise records request returns roughly schema service yet` |
| `P1-15` | Paper 1 | D2 | 40 | A telehealth assistant asks a caller to restate… | `already applies asks assistant both call caller ceiling contact earlier every first fix given holds reads replica resolution restate session sla store symptom telehealth token transcript turns` |
| `P1-16` | Paper 1 | D2 | 44 | A coding assistant appends a short per-repository preference… | `after ahead appends assistant banner block both call change coding cost diagnostic each every first fixes forty guide miss opens per preference repository session short style target thousand time token unchanged volume` |
| `P1-17` | Paper 1 | D2 | 36 | A pricing tool ranks five supplier quotes against… | `against approval audits change committee contradict criteria different documented each five four identical inputs orderings pricing quotes ranking ranks return run several supplier tool weighted weighting` |
| `P1-18` | Paper 1 | D2 | 37 | A compliance assistant reviews a lengthy merger agreement,… | `agreement always assistant audits change clearance clears closing comfortably compliance context every flags issues lengthy merger middle opening regulator reliably reviews sections untouched window within` |
| `P1-19` | Paper 1 | D2 | 45 | A supply-chain dispute chat nears its token ceiling.… | `ceiling chain chat correctly dispute drifting each exact few file fixes keeps last message nears needs number numbers opening order print purchase regenerates still strategy summary supply time token turns typed` |
| `P1-20` | Paper 1 | D3 | 39 | An agent posted an approval request into the… | `across after agent another approval cannot change compliance confusing facilities finance fits function holds named one personnel posted reach request requires similarly six system tools twenty two wrong` |
| `P1-21` | Paper 1 | D3 | 37 | A pre-launch security review of a claims assistant… | `action append assistant claims closes delete demonstrable documented exposes finds gap hard integration launch least operations pre privilege read records regulator requires review security workflows` |
| `P1-22` | Paper 1 | D3 | 38 | A retrieval pipeline has always run right against… | `400ms 600ms 900ms accuracy against always below change contractual correct cut has hop measured measures p95 pipeline points redundant removing reranking retrieval right run sits six sla stage target` |
| `P1-23` | Paper 1 | D3 | 40 | A platform serves four million requests monthly under… | `baseline budget characterize distributions fire fits fixed four guardrails kept million monthly now one percent platform policy requests roughly sample sampling serves stabilize storage team trace uniform` |
| `P1-24` | Paper 1 | D3 | 40 | A retrieval system indexes a policy manual whose… | `answer audits clause clauses design each editions fits has heading hierarchy indexes ingestion jurisdictional manual numbered policy quarterly regulator retained retrieval revised sit superseded system three used` |
| `P1-25` | Paper 1 | D3 | 40 | Retrieval must match data shape and query pattern.… | `000 answers ask citing concepts counts data handbook index lexical lookups match number numbers one part pattern prose queries query retrieval select separate serves service shape table transactions two users` |
| `P1-26` | Paper 1 | D3 | 39 | Integration mechanism follows who decides what happens next.… | `900ms account applied assistant attributes budget cannot decides enumerate every fits follows gateway happens holds identifier integration mechanism next record request service supplies tier` |
| `P1-27` | Paper 1 | D3 | 41 | Adding a tenth system's tool definitions would push… | `adding agent already approach available block budget call context definitions deployed exactly fastest fits has logs model nine one past push sessions show system team tenth though tool tools usage` |
| `P1-28` | Paper 1 | D3 | 40 | Entitlement must constrain what is retrievable. A support… | `400 added bot chunks constrain entitlement field fill filter fix held index migration one other post retrievable retrieves strips support tenant tenants top until works` |
| `P1-29` | Paper 1 | D3 | 40 | Latency is defined by what the consumer does.… | `000 answers arrive assistant call case change completion consumer defined filed fits four latency p95 read record second slow staff writes` |
| `P1-30` | Paper 1 | D3 | 40 | Observability must explain why, not what. A three-agent… | `agent agents approves change claims clause clauses compliance escalate explain helps intake logging observability one outcome pipeline process retrieves share sometimes three trace used version` |
| `P1-31` | Paper 1 | D3 | 40 | Context belongs in the vector. Fixed windows cut… | `belongs blocking boundaries clauses context cut fix fixed has heading ingestion metadata mid moved off onto paths queries retrieval returns safety seams section sentence sign since sit unembedded vector windows works wrong` |
| `P1-32` | Paper 1 | D4 | 32 | A capability automating a manual review step enters… | `accuracy approach approve automating capability compliance enters error first manual measured month never next owner pilot rate review sets step threshold` |
| `P1-33` | Paper 1 | D4 | 38 | A summarization capability faces a compliance owner's sign-off… | `capability classes compliance composed drafted evaluation faces failures fall four has month next ninety off owner pilot production recurring set sign specification summarization traffic triaged` |
| `P1-34` | Paper 1 | D4 | 42 | A prompt edit produced better answers on ten… | `answers average better channel combined conversations edit forty hand handling live per picked plan produced prompt randomized request select sends sessions straight team ten test thousand tracking two weekly` |
| `P1-35` | Paper 1 | D4 | 44 | A legal-research assistant began citing a vacated ruling… | `assistant auditor began citations citing compliance controlling evaluation first index legal measured migrated model new newer precedent production research reviews ruling store unchanged vacated week weekly while` |
| `P1-36` | Paper 1 | D4 | 37 | A support-triage service must hold p95 latency and… | `account across applies change cost documents fits five floor four hold latency multi need p95 per policy quality questions reasoning request rest routine service step still support target tickets triage while` |
| `P1-37` | Paper 1 | D4 | 40 | A thumbs-down rate stepped up on one day… | `aggregate change comes dashboard day down final first instrumentation limit one outputs quality rate regulated releases reports retention shipped single stepped store stored three thumbs timestamps` |
| `P1-38` | Paper 1 | D4 | 40 | Every record a nightly loader accepts must match… | `accepts agrees arrive check closely enforces every grader human labels loader machine match million monthly nightly published readable record records regulator required sampling schema structure two` |
| `P1-39` | Paper 1 | D4 | 37 | A regulated lender's assistant drafts personalized customer messages… | `assistant auditor contain customer discriminatory documents drafts evidence fee invoke language lender measure message messages monthly party personalized policy regulated requires retrieved reviews team third tool waiver` |
| `P1-40` | Paper 1 | D4 | 39 | After onboarding a client whose filings are mostly… | `accuracy after case checked client commitment contractual document escalations fifty filings first frequency historical index mirrors model mostly onboarding prompt rarest reports rose set type unchanged` |
| `P1-41` | Paper 1 | D4 | 39 | One variant changed prompt, model, and retrieval depth.… | `arms both changed cost day depth end first four fourteen guardrails held latency metric model one open planned points primary prompt retrieval rose stayed team variant` |
| `P1-42` | Paper 1 | D5 | 40 | A governance standard requires that safety controls fail… | `approves assistant change confirmation content control controls fail filter finance governance human independently limit orders places post procurement requires response safety satisfies standard supplier unattended` |
| `P1-43` | Paper 1 | D5 | 40 | A regulator's code discourages account identifiers reaching an… | `absolute account approved clause code conformance control counsel discourages endpoint enforces finds has identifiers inference outbound rate reaching region regulator requests ruled runs sampling satisfies` |
| `P1-44` | Paper 1 | D5 | 42 | An email-drafting agent began appending an unrequested signature… | `agent appending arbitrary began changed code drafting email every external forwarded has investigate just line messages nothing processing prompt quote reply review select signature started text two unrequested week` |
| `P1-45` | Paper 1 | D5 | 36 | A triage assistant classifies 12,000 claims daily at… | `000 accuracy appealable assistant claims classifies corrections daily denials each externally fits funded handling items nine ninety policy reversible review reviewers routing shift triage trivially visible` |
| `P1-46` | Paper 1 | D5 | 40 | A benefit-triage model's per-group false-negative rates were signed… | `annotation appeals audit benefit cases clustering comes disparity false first forty found giving group language launch model negative off ombudsman per population proportional rates reports set signed smallest step triage` |
| `P1-47` | Paper 1 | D5 | 38 | A certification audit finds a reporting agent calling… | `agent already audit calling catalogue certification change duplicates each every finds ingestion one performs reporting require revertible run service tool versioned write writes` |
| `P1-48` | Paper 1 | D5 | 39 | A support assistant is to be built on… | `approve assistant built compliance covered dataset design evaluation health holds index officer patient patients proceeds provider records residents seeded support vector` |
| `P1-49` | Paper 1 | D5 | 40 | A platform inventory finds request and response bodies… | `accept access bodies carry closed data design finds indefinitely inventory last legal miss month near personal platform purpose question raised regulated request response restricted retained retention review stated` |
| `P1-50` | Paper 1 | D5 | 39 | A pre-launch review covers an agent that triages… | `account agent approve bodies closes control covers credits customer email exposure finance followed hidden holds inbound instructions issuing launch messages pre red review team tool triages unattended` |
| `P1-51` | Paper 1 | D6 | 35 | A sponsor asks the architect to fix the… | `already approved architect asks backlog budget citing desk first fix has leadership level pipeline retrieval sponsor staffing stayed support ticket tripled volume` |
| `P1-52` | Paper 1 | D6 | 43 | A compliance officer preparing a regulatory filing already… | `accuracy against already architect claim compliance fallen figures filing has last multi officer party per plan planning preparing provide quarter reflect regulatory shift since submission though type yet` |
| `P1-53` | Paper 1 | D6 | 42 | A client negotiating a content-moderation contract insists on… | `architect client content contract contractually cover expand fixed flat guarantee insists markets mix moderation monitored negotiating new precision propose though today yet` |
| `P1-54` | Paper 1 | D6 | 44 | An architect documents why a team routed low-risk… | `accuracy architect ceiling compute contain cost documentation documents edge finance had held larger low mandated model out queries risk routed routing scored set small smaller team though tier` |
| `P1-55` | Paper 1 | D6 | 39 | A system supporting a regulated product line was… | `alongside already batch climbing complaints delay documentation error handed internal job line operations product rate regulated repository rise select session supporting system team traced training two unrelated` |
| `P1-56` | Paper 1 | D6 | 35 | A legal-operations lead wants a contract-review triage tool… | `acceptable architect before begins closes contract cycle design discussed false has lead legal live negative operations rate renewal review six though tool triage vendor wants weeks yet` |
| `P1-57` | Paper 1 | D6 | 39 | A transaction-monitoring system flags money laundering for a… | `100 alert alerts already bank case compliance costs false flags investigate investigators laundering missed money monitoring off overwhelmed set sign system though threshold times transaction` |
| `P1-58` | Paper 1 | D6 | 37 | A product owner asks why a loan-approval assistant… | `all applications approval architect asks assistant cases covers currently explain human loan low off owner product regulator required risk routes sign still though threshold underwriters value` |
| `P1-59` | Paper 1 | D6 | 45 | Three weeks after a team takes over the… | `400ms after begin bring ceiling change changed check configuration failing first have input latency mix model outputs p95 pipeline sla subset takes team though three value weeks` |
| `P1-60` | Paper 1 | D7 | 37 | A skill scoped only to draft dependency-update pull… | `before command context database dependency diff draft exploration final freeze migration model out pull pushed ran recently release requests scoped select skill step two unchanged update version` |
| `P1-61` | Paper 1 | D7 | 37 | An engineering team must split a monolithic billing… | `acquisition across application approved before billing boundaries debate dozen engineering files final has last lead many monolithic off platform quarter recent reopened services sign split team though two using` |
| `P1-62` | Paper 1 | D7 | 40 | A healthcare pipeline's data-export tool must never run,… | `ahead attempt audit compliance contractor data every export follow healthcare holds manual needs never pipeline record regulatory relying reviewer run select session team tool triggered two unprompted without` |
| `P1-63` | Paper 1 | D7 | 42 | A nightly batch job that drafts customer responses… | `ahead batch change claude closes code compliance correctly customer default drafts engineers five gap identical identifiers job mask masks never nightly responses review run sessions though through version` |

## Append rule

A shipped paper appends 63 rows here, ids `P<N>-01` through `P<N>-63`, before the paper is recorded
as generated in `EXAM-LOG.md`. The ledger is rebuilt from the shipped HTML files, never from the
generating session's own list.
