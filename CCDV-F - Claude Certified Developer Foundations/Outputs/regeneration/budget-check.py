# CCDV-F design v2 budget check
# Verifies: chapter sums, per-skill totals vs published share, +-20% rule, domain rollup.

SKILL_WEIGHT = {  # published %, from EXAM-FACTS_v1.md section 2
    "Agent Architecture": 4.5, "Agent Construction": 5.3, "Agent Patterns": 4.9,
    "Claude App Design": 8.6, "SWE Foundations": 7.4, "Claude API Mechanics": 6.8,
    "Configuration Mgmt": 4.1, "Understanding Requirements": 3.4, "Systems Life Cycle": 2.8,
    "Claude Code Operation": 3.1,
    "Debugging": 2.6,
    "Technical Fundamentals": 6.1, "LLM Fundamentals": 5.2, "Cost and Token Mgmt": 2.8,
    "Model Selection": 2.7,
    "Prompt Engineering": 4.6, "Context Engineering": 3.8, "Output Handling": 2.6,
    "AI Application Security": 3.2, "Guardrails": 2.3, "Identity Secrets Keys": 1.6,
    "Claude Hooks": 1.0,
    "Tool Implementation": 4.4, "Agentic Customization": 4.1, "MCP Server Development": 2.1,
}

DOMAIN = {
    1: ["Agent Architecture", "Agent Construction", "Agent Patterns"],
    2: ["Claude App Design", "SWE Foundations", "Claude API Mechanics",
        "Configuration Mgmt", "Understanding Requirements", "Systems Life Cycle"],
    3: ["Claude Code Operation"],
    4: ["Debugging"],
    5: ["Technical Fundamentals", "LLM Fundamentals", "Cost and Token Mgmt", "Model Selection"],
    6: ["Prompt Engineering", "Context Engineering", "Output Handling"],
    7: ["AI Application Security", "Guardrails", "Identity Secrets Keys", "Claude Hooks"],
    8: ["Tool Implementation", "Agentic Customization", "MCP Server Development"],
}
DOMAIN_PUB = {1: 14.7, 2: 33.1, 3: 3.1, 4: 2.6, 5: 16.8, 6: 11.0, 7: 8.1, 8: 10.6}

# ch -> (total_words, {skill: words})   * = changed from v1
CH = {
 1:  (2400, {"LLM Fundamentals":1600, "Context Engineering":800}),
 2:  (1600, {"LLM Fundamentals":1600}),
 3:  (2600, {"Model Selection":1800, "LLM Fundamentals":800}),
 4:  (3100, {"Technical Fundamentals":2400, "Claude API Mechanics":700}),      # * +700 Bedrock/Vertex
 5:  (2600, {"Technical Fundamentals":1800, "SWE Foundations":800}),
 6:  (3400, {"Prompt Engineering":3000, "LLM Fundamentals":400}),              # * +400 restore
 7:  (2200, {"Output Handling":2200}),
 8:  (2400, {"Context Engineering":2400}),
 9:  (2200, {"Cost and Token Mgmt":2200}),
 10: (2200, {"Tool Implementation":1400, "Claude API Mechanics":800}),
 11: (2200, {"Tool Implementation":2200}),
 12: (1800, {"Claude API Mechanics":1800}),
 13: (2400, {"Agentic Customization":2400}),
 14: (2600, {"MCP Server Development":1800, "Agentic Customization":800}),
 15: (3200, {"Agent Architecture":2200, "Agent Patterns":1000}),
 16: (3400, {"Agent Construction":2600, "Agent Patterns":800}),                # * +800 frameworks
 17: (1800, {"Agent Construction":1400, "Agent Patterns":400}),
 18: (2200, {"Agent Patterns":1800, "Claude Code Operation":400}),
 19: (1800, {"Agent Architecture":900, "Claude Hooks":900}),
 20: (2600, {"Claude Code Operation":2600}),
 21: (3300, {"Configuration Mgmt":2700, "Claude Code Operation":600}),
 22: (3000, {"Claude App Design":3000}),                                       # * +200
 23: (2200, {"Claude App Design":2200}),                                       # * split of old ch23
 24: (1800, {"Claude App Design":1800}),                                       # * split of old ch23
 25: (2200, {"Claude API Mechanics":2200}),
 26: (1800, {"Debugging":1800}),
 27: (1800, {"Debugging":1800}),
 28: (1400, {"Debugging":1400}),
 29: (2900, {"AI Application Security":2900}),                                 # * +900 PII/leakage/integrity/jailbreak
 30: (1300, {"Guardrails":1300}),                                              # * NEW chapter
 31: (2400, {"Identity Secrets Keys":1200, "Guardrails":800,
             "Claude API Mechanics":400}),
 32: (1900, {"Understanding Requirements":1900}),
 33: (2000, {"SWE Foundations":2000}),
 34: (2800, {"SWE Foundations":1400, "Systems Life Cycle":1400}),
}

errs = []
for ch, (tot, attrib) in CH.items():
    if sum(attrib.values()) != tot:
        errs.append(f"ch{ch}: attributions {sum(attrib.values())} != total {tot}")
if errs:
    print("ATTRIBUTION MISMATCH:"); [print(" ", e) for e in errs]
else:
    print("Attribution consistency: all %d chapters OK" % len(CH))

TOTAL = sum(t for t, _ in CH.values())
print(f"\nTOTAL BUDGET: {TOTAL:,} words across {len(CH)} chapters "
      f"(avg {TOTAL//len(CH):,}, max {max(t for t,_ in CH.values()):,})")
assert abs(sum(SKILL_WEIGHT.values()) - 100.0) < 0.05, sum(SKILL_WEIGHT.values())

got = {s: 0 for s in SKILL_WEIGHT}
for _, attrib in CH.values():
    for s, w in attrib.items():
        got[s] += w

print("\n%-28s %6s %8s %8s %8s  %s" % ("SKILL", "pub%", "share", "alloc", "delta", "flag"))
breaches = []
for s, pct in sorted(SKILL_WEIGHT.items(), key=lambda x: -x[1]):
    share = pct / 100 * TOTAL
    d = (got[s] - share) / share * 100
    flag = "BREACH" if abs(d) > 20 else ""
    if flag:
        breaches.append((s, round(d, 1)))
    print("%-28s %6.1f %8.0f %8d %+7.1f%%  %s" % (s, pct, share, got[s], d, flag))

print("\n%-34s %8s %8s %8s %7s" % ("DOMAIN", "words", "course%", "pub%", "delta"))
for d, skills in DOMAIN.items():
    w = sum(got[s] for s in skills)
    print("%-34s %8d %7.1f%% %7.1f%% %+7.1fpp"
          % (f"{d}", w, w / TOTAL * 100, DOMAIN_PUB[d], w / TOTAL * 100 - DOMAIN_PUB[d]))

print("\n+-20%% BREACHES: %s" % (breaches if breaches else "none"))
