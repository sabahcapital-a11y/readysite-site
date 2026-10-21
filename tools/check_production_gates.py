#!/usr/bin/env python3
"""ReadySite release gate status — fails intentionally while any required gate is blocked.
Run locally: python3 tools/check_production_gates.py
"""
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "READY_SITE_OFFER_MANIFEST.json").read_text(encoding="utf-8"))
gates = json.loads((root / "READY_SITE_RELEASE_GATES.json").read_text(encoding="utf-8"))
valid_states = {"blocked", "verified", "not_applicable"}
issues = []
entries = gates.get("gate_definitions", [])
ids = [g.get("id") for g in entries]
if not entries or len(ids) != len(set(ids)):
    issues.append("Release gate list missing or duplicate gate IDs.")
if gates.get("business") != "ReadySite":
    issues.append("Wrong business scope.")
if not isinstance(gates.get("production_release_authorized"), bool):
    issues.append("Approval field must be boolean.")
for g in entries:
    if g.get("state") not in valid_states:
        issues.append("Invalid state on " + str(g.get("id")))
    if not g.get("evidence") or not g.get("owner_action"):
        issues.append("Missing evidence/action on " + str(g.get("id")))
blocked = [g for g in entries if g.get("state") == "blocked"]
for g in blocked:
    print("BLOCKED:", g["id"], "-", g["name"])
if not gates.get("production_release_authorized"):
    issues.append("Owner release approval not recorded.")
for flag in ("payment_enabled", "inquiries_enabled", "public_deployment_approved"):
    if manifest.get(flag) is not True:
        issues.append("Manifest launch capability not enabled: " + flag)
if blocked:
    issues.append(str(len(blocked)) + " unresolved release gates.")
for issue in issues:
    print("NOT READY:", issue)
if issues:
    print("RESULT: NOT PRODUCTION READY")
    sys.exit(1)
print("RESULT: METADATA CLAIMS READY. Independently verify external evidence before deploying.")
