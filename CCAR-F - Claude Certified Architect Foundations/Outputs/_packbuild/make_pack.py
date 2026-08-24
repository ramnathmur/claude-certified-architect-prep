#!/usr/bin/env python3
"""One command to build, remap and verify the whole pack.

Order matters: build_pack wipes and repopulates the folder, remap_deck rewrites the drill
deck's question map to match the papers that were just written, and verify_pack re-reads
everything from scratch. Any step failing stops the run.
"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = [("build",  "build_pack.py"),
         ("remap",  "remap_deck.py"),
         ("verify", "verify_pack.py")]

for label, script in STEPS:
    print(f"\n{'='*70}\n== {label}: {script}\n{'='*70}")
    r = subprocess.run([sys.executable, os.path.join(HERE, script)])
    if r.returncode != 0:
        sys.exit(f"\n{label} FAILED (exit {r.returncode}) -- pack is not shippable")
print("\n" + "=" * 70)
print("PACK BUILT, REMAPPED AND VERIFIED")
