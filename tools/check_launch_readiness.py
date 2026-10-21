#!/usr/bin/env python3
"""ReadySite prelaunch verification. Exit 0 = staged preview safe, NOT production ready."""
from pathlib import Path
from html.parser import HTMLParser
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
HOME = (ROOT / "index.html").read_text(encoding="utf-8")
INTAKE = (ROOT / "intake-preview.html").read_text(encoding="utf-8")
MANIFEST = json.loads((ROOT / "READY_SITE_OFFER_MANIFEST.json").read_text(encoding="utf-8"))
failures = []
blockers = []

class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = 0
        self.active_submit_buttons = 0
        self.links = []
        self.script_sources = []
        self.meta_robots = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "form":
            self.forms += 1
        if tag == "script" and "src" in a:
            self.script_sources.append(a["src"])
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag == "button":
            if a.get("type", "submit") == "submit" and "disabled" not in a:
                self.active_submit_buttons += 1
        if tag == "meta" and a.get("name") == "robots":
            self.meta_robots.append(a.get("content", ""))

def check(condition, why):
    if not condition:
        failures.append(why)

home = PageInspector()
home.feed(HOME)
intake = PageInspector()
intake.feed(INTAKE)

pilot = next((x for x in MANIFEST.get("offers", []) if x.get("id") == "website_pilot"), None)
check(bool(pilot), "Offer manifest missing website_pilot.")
if pilot:
    check(pilot.get("status") == "proposed_not_for_sale", "Pilot must not be listed as selling.")
    check("$" + str(pilot.get("setup_usd")) in HOME, "Homepage setup and manifest mismatch.")
    check("$" + str(pilot.get("monthly_usd")) + "/month" in HOME, "Homepage monthly and manifest mismatch.")

for flag in ("payment_enabled", "inquiries_enabled", "outreach_authorized", "public_deployment_approved"):
    check(MANIFEST.get(flag) is False, "Release flag " + flag + " unexpectedly enabled.")

check("noindex,nofollow" in home.meta_robots, "Unreleased homepage should be noindex.")
check("noindex,nofollow" in intake.meta_robots, "Internal intake demo should be noindex.")
check(home.forms == 0 and home.active_submit_buttons == 0, "Homepage must not contain active forms.")
check(intake.forms == 1 and intake.active_submit_buttons == 1, "Intake demo must have exactly one sample-only form.")
check("e.preventDefault()" in INTAKE, "Intake demo should prevent submission.")
check("Customer submission disabled" in INTAKE, "Explicit intake submission disabled notice missing.")
check(not intake.script_sources, "Intake demo must not load outside scripts.")
check(not any(x.startswith(("mailto:", "tel:", "https://")) for x in intake.links), "Intake demo must not open external contact endpoints.")
check("fictional demonstrations" in HOME.lower(), "Fictional example disclosure missing.")
check("Online inquiries and payments are not active yet." in HOME, "Homepage prelaunch disclosure missing.")
for bad in ("Secure checkout by Stripe", "Live in 24 hours", "refund you in full", "pay only if you want to keep it", "24/7 AI receptionist"):
    check(bad.lower() not in HOME.lower(), "Disallowed claim: " + bad)

for name in ("terms.html", "refunds.html", "privacy.html"):
    content = (ROOT / name).read_text(encoding="utf-8")
    if "[DATE]" in content or "Contact: coming soon" in content or "DRAFT" in content:
        blockers.append(name + ": unfinished legal/contact content")
blockers.append("Existing local/ and guide pages require separate offer/copy/SEO review")
blockers.append("No verified business inbox, inquiry backend, payments or tested fulfillment")
blockers.append("Reported exposed token must be rotated; no access to external box to verify")

print("ReadySite staged preview safety checks")
for f in failures:
    print("FAIL:", f)
for b in blockers:
    print("RELEASE BLOCKER:", b)
print(str(len(failures)) + " staged-check failures; " + str(len(blockers)) + " production-release blockers")
if failures:
    sys.exit(1)
print("PASS: prelaunch preview only. NOT AUTHORIZED FOR PRODUCTION LAUNCH.")
