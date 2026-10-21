#!/usr/bin/env python3
"""ReadySite prelaunch truthfulness smoke checks. Run: python3 tools/check_launch_readiness.py"""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
home = (root / "index.html").read_text(encoding="utf-8")
config = json.loads((root / "READY_SITE_OFFER_MANIFEST.json").read_text(encoding="utf-8"))
errors = []
notes = []

def require(value, message):
    if not value:
        errors.append(message)

def deny(value, message):
    if value:
        errors.append(message)

pilot = next(item for item in config["offers"] if item["id"] == "website_pilot")
require(pilot["status"] == "proposed_not_for_sale", "Pilot must remain explicitly unsellable while prelaunch.")
require(f'${pilot["setup_usd"]}' in home, "Homepage setup price differs from manifest.")
require(f'${pilot["monthly_usd"]}/month' in home, "Homepage recurring price differs from manifest.")
require('noindex,nofollow' in home, "Staged page should not be indexed.")
require("fictional" in home.lower(), "Fictional demonstrations must be disclosed.")
require("Online inquiries and payments are not active yet." in home, "Truthful prelaunch disclosure missing.")
for phrase in ("Secure checkout by Stripe", "Live in 24 hours", "refund you in full", "pay only if you want to keep it", "24/7 AI receptionist"):
    deny(phrase.lower() in home.lower(), f"Unsupported homepage marketing claim: {phrase}")
deny(bool(re.search(r'<form\\b', home, flags=re.I)), "No unsupported form without a tested backend.")
deny(bool(re.search(r'mailto:|action=["\\\']https?://', home, flags=re.I)), "Do not invent communication endpoint.")
for field in ("payment_enabled","inquiries_enabled","outreach_authorized","public_deployment_approved"):
    require(config.get(field) is False, f"Blocked action prematurely enabled: {field}")

# This checker is not a comprehensive launch certification.
legacy = [root / x for x in ["terms.html","refunds.html","privacy.html"]]
for path in legacy:
    if path.exists():
        contents = path.read_text(encoding="utf-8")
        if "[DATE]" in contents or "Contact: coming soon" in contents:
            notes.append(f"BLOCKER: {path.name} contains incomplete legal/contact placeholders.")
if (root / "local").exists():
    notes.append("BLOCKER: local/ and guides/ have not been validated against current offer manifest.")
print("ReadySite prelaunch smoke-check")
for n in notes:
    print(n)
for e in errors:
    print("FAIL:", e)
print(f"Result: {len(errors)} smoke-check failures; {len(notes)} unresolved release blockers.")
sys.exit(1 if errors else 0)
