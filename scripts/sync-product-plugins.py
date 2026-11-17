#!/usr/bin/env python3
"""Copy the shared skills from chargezen/ into each product plugin.

chargezen/skills/ is the only place to edit a skill. Each product plugin carries
the shared `chargezen` rules plus the job skills whose tools its product address
offers (https://chargezen.com/developers/mcp lists each address's tools).

  scripts/sync-product-plugins.py          copy the skills
  scripts/sync-product-plugins.py --check  fail if any copy differs (CI runs this)
"""
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "chargezen" / "skills"

# Plugin -> job skills that work on its address. Every plugin also gets `chargezen`.
PRODUCT_SKILLS = {
    "chargezen-subscriptions": ["subscribe-and-save", "loyalty-review", "subscription-help", "next-order", "new-subscription", "cancellations"],
    "chargezen-concierge": ["inbox-triage", "loyalty-review"],
    "chargezen-smartytap": ["campaign", "inbox-triage"],
    "chargezen-spark": ["creator-review"],
}


def expected_files():
    for plugin, skills in PRODUCT_SKILLS.items():
        for skill in ["chargezen", *skills]:
            yield SOURCE / skill / "SKILL.md", ROOT / plugin / "skills" / skill / "SKILL.md"


def stray_skills():
    for plugin, skills in PRODUCT_SKILLS.items():
        wanted = {"chargezen", *skills}
        for folder in (ROOT / plugin / "skills").glob("*"):
            if folder.name not in wanted:
                yield folder


def check():
    drift = [str(copy.relative_to(ROOT)) for source, copy in expected_files()
             if not copy.exists() or not filecmp.cmp(source, copy, shallow=False)]
    drift += [f"{folder.relative_to(ROOT)} (not in PRODUCT_SKILLS)" for folder in stray_skills()]
    if drift:
        print("Product plugin skills differ from chargezen/skills. Run scripts/sync-product-plugins.py:")
        print("\n".join(f"  {path}" for path in drift))
        return 1
    print("Product plugin skills match chargezen/skills.")
    return 0


def sync():
    for source, copy in expected_files():
        copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, copy)
    for folder in stray_skills():
        shutil.rmtree(folder)
    return check()


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv[1:] else sync())
