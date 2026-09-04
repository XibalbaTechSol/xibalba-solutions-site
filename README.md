# Xibalba Solutions Website

Public marketing site for **Xibalba Solutions**, at [xibalbatechsol.github.io/xibalba-solutions-site](https://xibalbatechsol.github.io/xibalba-solutions-site/). Static HTML/CSS/JS, no build step, no framework.

The homepage (`index.html`) functions as a **gateway to two open-source products**:

- **[Xibalba Cortex](https://github.com/XibalbaTechSol/xibalba-cortex)** — provenance-aware, hash-chained agent memory (MCP server)
- **[Xibalba Shield](https://github.com/XibalbaTechSol/xibalba-shield)** — Linux endpoint agent-security sensor (eBPF + OPA policy)

Both are built on **[Integrity Core](https://github.com/XibalbaTechSol/integrity-core)**, an on-chain protocol for agent identity/reputation, but neither requires it — the homepage frames Integrity Core as the backbone underneath, not the lead product. All three repos are independently open source; this site links out to them rather than re-hosting their docs.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | Homepage — the Cortex/Shield/Integrity Core gateway. The only page meant to sell the three products; everything else is legacy/secondary content, see below. |
| `about.html`, `ai-agents.html`, `hermes-swarm.html`, `integrity-coin.html`, `integrity-protocol.html`, `local-ai.html`, `sanctum-brain.html`, `pricing.html` | Older pages from a prior positioning ("Sovereign AI Intelligence" / Hermes agents / OpenClaw). Still live and linked from `index.html`'s footer/nav in some cases, but not part of the current homepage pitch — content may be stale relative to `index.html`. Don't assume these describe the current product lineup. |
| `contact.html`, `thank-you.html`, `privacy.html` | Contact flow and legal boilerplate. |
| `blog.html` + `blog/` | Blog index and generated posts (see **Blog management** below). Posts are from the prior positioning era — none currently reference Cortex/Shield/Integrity Core. |
| `css/style.css`, `js/main.js` | Site-wide styles and behavior (hamburger nav, contact-form submission, `CONTACT_ENDPOINT`). |
| `server.py` | Backend for the `/contact` POST route only — see **Deployment**, this does NOT serve the static pages in production. |
| `render.yaml` | Render.com Blueprint for deploying `server.py` as a Web Service. |
| `.env.example` | Template for `server.py`'s SMTP/CORS config — copy to `.env` for local dev. |
| `tests/`, `test_a11y.py` | Ad hoc Playwright UI/accessibility checks (see **Testing**) — not a maintained regression suite, expect some to reference stale content from the prior positioning era. |
| `scripts/` | One-off screenshot/chart/doc-generation utilities used during past redesign passes, not part of any regular workflow. |
| `docs/` | Static assets (whitepaper/business-plan PDFs) — not currently linked from `index.html`. |
| `.Jules/palette.md` | Notes left by an automated PR bot (see **Known note: the Palette bot** below). |

## Development

### Prerequisites

- Python 3.12+
- SMTP credentials, only if you want to test actual email delivery from `/contact` locally

### Local setup

```bash
git clone https://github.com/XibalbaTechSol/xibalba-solutions-site.git
cd xibalba-solutions-site
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in SMTP_* if you want /contact to actually send mail
python3 server.py
```

Visit `http://localhost:8000` — this serves both the static pages and `/contact` locally, matching production's *content* even though production splits the two across different hosts (see **Deployment**).

`.env` variables `server.py` reads:

| Variable | Default | Notes |
|---|---|---|
| `SMTP_SERVER` | `localhost` | |
| `SMTP_PORT` | `587` | |
| `SMTP_USER` | *(empty)* | If unset (with `SMTP_PASS`), `/contact` attempts unauthenticated local SMTP instead. |
| `SMTP_PASS` | *(empty)* | Gmail App Password if using `smtp.gmail.com`. |
| `FROM_EMAIL` | `relay@xibalbasolutions.com` | |
| `ALLOWED_ORIGIN` | `https://xibalbatechsol.github.io` | CORS origin allowed to call `/contact` cross-origin — must match wherever the static pages are actually served from. |
| `PORT` | `8000` | |

### Blog management

Posts live as Markdown in `blog/src/`, with frontmatter:

```markdown
---
title: "Your Post Title"
date: "YYYY-MM-DD"
category: "TECH/ARCHITECTURE/PRIVATE"
excerpt: "A short summary for the index page."
---
Your content here...
```

Run `python3 manage_blog.py` to regenerate `blog/*.html` and `blog.html`'s index from `blog/src/*.md` via `blog/templates/post_template.html`. The converter (`manage_blog.py`) is a minimal hand-rolled Markdown-to-HTML pass, not a full Markdown implementation — check its output for anything beyond basic formatting.

### Testing

```bash
pip install pytest playwright pytest-playwright
playwright install chromium
pytest
# or:
./run_all_ui_tests.sh
```

`tests/` and root-level `test_a11y.py` are ad hoc Playwright checks accumulated across redesign passes (UI/UX per-page smoke tests, mobile nav, a11y). They are **not a maintained regression suite** — several (`test_second_brain.py`, references inside `test_index.py`/`test_site.py`) predate the current homepage content and may assert against markup that no longer exists. Treat a failure as a prompt to check whether the test or the page is stale, not as an automatic bug.

## Deployment

**The static pages and the `/contact` backend deploy to two different places** — GitHub Pages can't run `server.py` (Python), so the split is real, not incidental:

- **Static pages** → GitHub Pages, building from `main` / root on every push. `index.html`, `js/main.js`, and every other page are served from `https://xibalbatechsol.github.io/xibalba-solutions-site/`.
- **`/contact` backend** → Render.com Web Service (`render.yaml`), running `python server.py`. Live at `https://xibalba-solutions-site.onrender.com`. `js/main.js`'s `CONTACT_ENDPOINT` constant and `contact.html`'s `<form action>` both point here explicitly — update both together if this URL ever changes, and update `ALLOWED_ORIGIN` on the Render side to match if the static host ever changes.
- `server.py` uses `socketserver.ThreadingTCPServer` (not plain `TCPServer`) and an explicit `timeout=10` on outbound SMTP — both fixed after being caught live: a single held-open connection was blocking every other request, and Render's network silently drops (rather than refuses) outbound SMTP, which used to hang requests indefinitely. Keep both if you ever touch this file.
- **Known gap:** Render's outbound network blocks SMTP entirely (confirmed via `[Errno 101] Network is unreachable`, not an auth failure) — `/contact` currently fails cleanly rather than sending mail. Fixing this for real means switching to an HTTPS-based email API (SendGrid/Mailgun/Resend) rather than raw SMTP; not yet done.

**Known note: two GitHub Pages deployment mechanisms are both currently configured** — a legacy branch-based build (`Settings → Pages → source: main / root`, GitHub API reports `build_type: "legacy"`) and `.github/workflows/static.yml` (an Actions-based `actions/deploy-pages` workflow that also runs and succeeds on every push). Both have been deploying successfully in parallel without visible conflict, but this is redundant and worth consolidating to one mechanism rather than relying on both continuing to agree.

**Known note: the Palette bot.** `.Jules/palette.md` and repeated `🎨 Palette: ...` PR titles come from an automated Google Jules agent that opened ~130 near-duplicate PRs (mostly re-proposing already-shipped accessibility/UX fixes) daily from February through September 2026 without any apparent memory of its own prior PRs. All were closed 2026-09 after verifying each one against current `main`. If you see a fresh wave of `Palette` PRs, check whether the underlying fix is already on `main` before merging — don't assume novelty from the PR title alone.

### Sovereign VPS

For full data-sovereignty deployment (both static + backend on infrastructure you control), a Docker/VPS host capable of running `server.py` directly is the alternative to the GitHub Pages + Render split above.

## License

All rights reserved. © 2026 Xibalba Solutions.
