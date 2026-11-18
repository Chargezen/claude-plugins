#!/usr/bin/env python3
"""Build the ChatGPT (OpenAI Agent Plugins) ZIP for the full Chargezen connector.

openai/chargezen/ holds what is only in the ChatGPT package: plugin.json, mcp.json,
assets/ and the get-started onboarding skill. The job skills are copied from
chargezen/skills/ on every build, so chargezen/skills/ stays the only place to edit
a skill. The copies are rewritten to read correctly in ChatGPT (see transform()).

  scripts/build-openai-plugin.py                 build dist/chargezen-openai-plugin.zip
  scripts/build-openai-plugin.py --out PATH.zip  also copy the ZIP to PATH.zip

The build validates the package against the limits in
https://developers.openai.com/plugins/deploy/submission and .../submission-errors
and fails on any problem.
"""
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "openai" / "chargezen"
SKILLS = ROOT / "chargezen" / "skills"
DIST = ROOT / "dist"
ZIP = DIST / "chargezen-openai-plugin.zip"

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
KEPT_KEYS = ("name", "description")


def transform(name, text):
    """Rewrite a Claude Code skill so it reads correctly in ChatGPT."""
    match = FRONTMATTER.match(text)
    fields = dict(re.findall(r"^([A-Za-z_-]+): ?(.*)$", match.group(1), re.M))
    # Only name and description are skill frontmatter in OpenAI packages; Claude's
    # argument-hint has no meaning there.
    head = "---\n" + "".join(f"{key}: {fields[key]}\n" for key in KEPT_KEYS) + "---\n"
    body = text[match.end():]

    # $ARGUMENTS is Claude Code's slash-command input; in ChatGPT the request is the
    # conversation itself.
    body = body.replace("the last $ARGUMENTS days", "the number of days the user asked for")
    body = body.replace("the next $ARGUMENTS days", "the number of days ahead the user asked for")
    body = re.sub(r"up to \$ARGUMENTS (\w+)", r"up to the number of \1 the user asked for", body)
    body = body.replace("$ARGUMENTS", "what the user asked for")

    # Products outside the full connector: this package already reaches every product.
    body = body.replace("(the `/win-back` skill, in the full Chargezen plugin)", "(the `win-back` skill)")
    body = body.replace("`/payment-recovery` (full Chargezen plugin)", "the `payment-recovery` skill")
    body = body.replace("suggest a teammate with the full Chargezen plugin handles it", "suggest a teammate handles it")
    body = body.replace(
        " A product plugin reaches only that product's tools (plus customers, products and loyalty where the "
        "product offers them); when a job needs another product, say so and suggest the `chargezen` plugin, "
        "which reaches every product.", "")
    body = body.replace("Every command in this plugin does one whole job", "Every other skill in this plugin does one whole job")
    body = body.replace("Every CheckoutOS job has its own command:", "Every CheckoutOS job has its own skill:")

    # Slash commands are skills here.
    body = re.sub(r"a (first|one-off) `/([a-z][a-z0-9-]*)`", r"a \1 \2 (the `\2` skill)", body)
    if name == "checkoutos":
        body = re.sub(r"`/([a-z][a-z0-9-]*)`", r"`\1`", body)
    body = re.sub(r"the `/([a-z][a-z0-9-]*)` skill", r"the `\1` skill", body)
    body = re.sub(r"the `/([a-z][a-z0-9-]*)` (steps|rules|launch steps)", r"the `\1` skill's \2", body)
    body = re.sub(r"\(`/([a-z][a-z0-9-]*)` steps", r"(the `\1` skill's steps", body)
    body = re.sub(r"`/([a-z][a-z0-9-]*)`", r"the `\1` skill", body)

    # Name the assistant neutrally.
    body = body.replace("and Claude can read and answer them there", "and you can read and answer them there through this connection")
    body = body.replace("Never suggest Claude can pay or mark a payout.", "Never suggest that you can pay or mark a payout.")

    description = fields["description"]
    description = description.replace("use /payment-recovery in the full Chargezen plugin", "use the payment-recovery skill")
    description = re.sub(r"`/([a-z][a-z0-9-]*)`", r"the \1 skill", description)
    description = re.sub(r"(?<![\w`])/([a-z][a-z0-9-]*)", r"the \1 skill", description)
    head = head.replace(f"description: {fields['description']}\n", f"description: {description}\n")

    out = head + body
    leftovers = re.findall(r"\$ARGUMENTS|Claude|argument-hint|(?<![\w/.`])/[a-z][a-z-]+(?=[`\s,.)])", out)
    if leftovers:
        raise SystemExit(f"skills/{name}: untransformed text {sorted(set(leftovers))}")
    return out


def assemble(stage):
    shutil.copytree(PACKAGE, stage, ignore=shutil.ignore_patterns(".DS_Store"))
    for skill in sorted(SKILLS.iterdir()):
        source = skill / "SKILL.md"
        if not source.is_file():
            continue
        target = stage / "skills" / skill.name
        if target.exists():
            raise SystemExit(f"skills/{skill.name} exists in both openai/chargezen and chargezen/skills")
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text(transform(skill.name, source.read_text()))
        for extra in skill.rglob("*"):
            if extra.is_file() and extra.name != "SKILL.md":
                dest = target / extra.relative_to(skill)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(extra, dest)


def png_size(path):
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def one_line(value, limit, label, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} is missing")
    elif "\n" in value or len(value) > limit:
        errors.append(f"{label} must be one line of at most {limit} characters ({len(value)})")


def validate(stage):
    errors = []
    manifest = json.loads((stage / "plugin.json").read_text())
    mcp = json.loads((stage / "mcp.json").read_text())

    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json $schema")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", manifest.get("name", "")) or len(manifest["name"]) > 64:
        errors.append("name must be lowercase letters, digits and single hyphens, at most 64 characters")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        errors.append("version must be a semantic version")
    if len(manifest.get("description", "")) > 1024:
        errors.append("description is over 1,024 characters")

    openai = manifest["extensions"]["com.openai"]
    ui = openai["interface"]
    one_line(ui.get("displayName"), 30, "displayName", errors)
    one_line(ui.get("shortDescription"), 30, "shortDescription", errors)
    one_line(ui.get("developerName"), 80, "developerName", errors)
    if not ui.get("longDescription") or len(ui["longDescription"]) > 4000:
        errors.append("longDescription must be 1 to 4,000 characters")
    categories = {"Productivity", "Creativity", "Developer Tools", "Business & Operations", "Data & Analytics",
                  "Communication", "Education & Research", "Security", "Finance", "Healthcare", "Travel",
                  "Entertainment", "Other"}
    if ui.get("category") not in categories:
        errors.append("category is not a supported category")
    capabilities = ui.get("capabilities", [])
    if len(capabilities) > 20:
        errors.append("more than 20 capabilities")
    for capability in capabilities:
        one_line(capability, 120, f"capability {capability!r}", errors)
    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        url = ui.get(field, "")
        if not url.startswith("https://") or len(url) > 1024 or "@" in url:
            errors.append(f"{field} must be an HTTPS URL of at most 1,024 characters")
    prompts = ui.get("defaultPrompt", [])
    if len(prompts) > 3 or len({p.strip().lower() for p in prompts}) != len(prompts):
        errors.append("defaultPrompt must be up to three unique prompts")
    for prompt in prompts:
        one_line(prompt, 128, f"defaultPrompt {prompt!r}", errors)
        if "@" in prompt:
            errors.append("defaultPrompt must not @mention")
    for field in ("brandColor", "brandColorDark"):
        if field in ui and not re.fullmatch(r"#[0-9A-Fa-f]{6}", ui[field]):
            errors.append(f"{field} must be #RRGGBB")

    paths = [ui[key] for key in ("composerIcon", "composerIconDark", "logo", "logoDark") if key in ui]
    if "composerIcon" not in ui or "logo" not in ui:
        errors.append("composerIcon and logo are required")
    for path in paths:
        file = stage / path
        if not path.startswith("./") or ".." in path or not file.is_file():
            errors.append(f"missing or invalid image path {path}")
            continue
        size = png_size(file)
        if not size or size[0] != size[1] or not 48 <= size[0] <= 4096 or file.stat().st_size > 5 * 1024 * 1024:
            errors.append(f"{path} must be a square PNG 48-4096 px, at most 5 MiB ({size})")

    onboarding = openai.get("onboardingSkill", "")
    if not onboarding.startswith("./") or not (stage / onboarding).is_file():
        errors.append(f"onboardingSkill {onboarding} is not in the package")

    for banned in ("apps", "hooks"):
        if banned in openai:
            errors.append(f"extensions.com.openai.{banned} is not allowed in a public submission")
    review = openai.get("review", {})
    for banned in ("test_credentials", "reviewer_instructions"):
        if banned in json.dumps(manifest):
            errors.append(f"{banned} must not be in the package")
    cases = review.get("test_cases", {})
    positive, negative = cases.get("positive", []), cases.get("negative", [])
    if len(positive) != 5 or len(negative) != 3:
        errors.append(f"need exactly 5 positive and 3 negative test cases ({len(positive)}, {len(negative)})")
    for case in positive:
        for key in ("description", "prompt", "tools_triggered", "expected_behavior"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                errors.append(f"positive case missing {key}")
        if len(case.get("description", "")) > 4000:
            errors.append("positive case description over 4,000 characters")
    for case in negative:
        for key in ("description", "prompt"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                errors.append(f"negative case missing {key}")
    if not openai.get("publication", {}).get("release_notes"):
        errors.append("publication.release_notes is missing")

    if mcp.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json":
        errors.append("mcp.json $schema")
    servers = mcp.get("mcpServers", {})
    if len(servers) != 1:
        errors.append("mcp.json must declare exactly one MCP server")
    for name, server in servers.items():
        if server.get("type") != "streamable-http" or not server.get("url", "").startswith("https://"):
            errors.append(f"MCP server {name} must be a remote streamable-http HTTPS server")
        if server.get("headers"):
            errors.append(f"MCP server {name} must not have headers")
        if "clientSecret" in json.dumps(server):
            errors.append(f"MCP server {name} must not carry a clientSecret")

    names = set()
    for skill in sorted((stage / "skills").iterdir()):
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        match = FRONTMATTER.match(text)
        if not match:
            errors.append(f"skills/{skill.name}: frontmatter missing or unclosed")
            continue
        fields = dict(re.findall(r"^([A-Za-z_-]+): ?(.*)$", match.group(1), re.M))
        if set(fields) != set(KEPT_KEYS):
            errors.append(f"skills/{skill.name}: frontmatter must hold only name and description ({sorted(fields)})")
        name = fields.get("name", "")
        if name != skill.name or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            errors.append(f"skills/{skill.name}: name {name!r} must match its folder")
        if len(f"{manifest['name']}:{name}") > 64:
            errors.append(f"skills/{skill.name}: plugin:skill name is over 64 characters")
        if name in names:
            errors.append(f"skills/{skill.name}: duplicate name")
        names.add(name)
        description = fields.get("description", "")
        if not description.strip() or len(description) > 1024:
            errors.append(f"skills/{skill.name}: description must be 1 to 1,024 characters")
        if not text[match.end():].strip():
            errors.append(f"skills/{skill.name}: body is empty")

    for file in stage.rglob("*"):
        rel = file.relative_to(stage).as_posix()
        if file.name in (".app.json", ".mcp.json", "hooks.json") or rel.startswith(("hooks/", ".codex-plugin/")):
            errors.append(f"{rel} must not be in the package")

    if errors:
        raise SystemExit("OpenAI plugin package is invalid:\n" + "\n".join(f"  {e}" for e in errors))
    return len(names)


def build(extra_out=None):
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp) / "chargezen"
        assemble(stage)
        skill_count = validate(stage)
        DIST.mkdir(exist_ok=True)
        ZIP.unlink(missing_ok=True)
        with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as archive:
            for file in sorted(stage.rglob("*")):
                if file.is_file():
                    archive.write(file, file.relative_to(stage).as_posix())
    print(f"Built {ZIP.relative_to(ROOT)} with {skill_count} skills.")
    if extra_out:
        shutil.copyfile(ZIP, extra_out)
        print(f"Copied to {extra_out}")


if __name__ == "__main__":
    args = sys.argv[1:]
    out = None
    if args[:1] == ["--out"] and len(args) == 2:
        out = Path(args[1])
    elif args:
        raise SystemExit(__doc__)
    build(out)
