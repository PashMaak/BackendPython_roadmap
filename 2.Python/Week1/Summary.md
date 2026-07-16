# Week 1 — Environment & Tooling — Conspect

## 1. Overview
This week's material isn't Python-the-language (already known) — it's the tooling layer everything else sits on: managing *which* Python interpreter runs (`pyenv`), and managing *which packages* are available to it (`pip`, virtual environments).

## 2. Glossary — state these precisely
- **pyenv** — a version manager that installs and switches between multiple Python interpreter versions on one machine, without touching the OS's system Python.
- **Virtual environment (venv)** — an isolated set of installed packages scoped to one project, independent of other projects on the same machine.
- **pip** — Python's package installer; fetches and installs packages from PyPI into whichever environment is currently active.
- **requirements.txt** — a plain-text list of a project's dependencies (often version-pinned), used to reproduce an environment elsewhere.
- **`pip freeze`** — dumps the exact versions of everything currently installed in the active environment, in `requirements.txt`-compatible format.

## 3. Core mechanisms
- [routine] `pyenv install <version>` builds/installs a specific interpreter; `pyenv global <version>` sets the machine-wide default, `pyenv local <version>` pins it per-directory.
- [**hard — most common confusion point**] pyenv and venv solve *different axes* of the same problem: pyenv picks **which interpreter**, venv (built from that interpreter) isolates **which packages**. They're chained, not interchangeable.
- [routine] `pip install X` always installs into whichever environment is *currently active* — system Python, a pyenv global, or an active venv. Always check which one that is before installing.
- [routine] `pip freeze > requirements.txt` snapshots exact versions; `pip install -r requirements.txt` reproduces that snapshot elsewhere.
- [hard] `pip freeze` captures *everything* installed, including transitive dependencies never explicitly requested — this is why `requirements.txt` files get bloated and OS-specific. (Tools like `pip-tools`/`poetry` fix this later — not needed yet.)

## 4. Procedures — reproduce these from memory
```bash
# pyenv: pick the interpreter
pyenv install 3.12.4          # example version — use whatever was actually installed
pyenv global 3.12.4           # or: pyenv local 3.12.4 (per-project)
pyenv versions                # list what's installed
python --version              # confirm what's active

# venv: isolate the packages
python -m venv .venv
source .venv/bin/activate     # Linux/macOS

# pip: manage packages
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt
```
*(Example — AI-generated: version number `3.12.4` is a placeholder, not a claim about what was installed.)*

## 5. Pitfalls — TRICKY
- Forgetting to `activate` the venv before `pip install` → package lands in the wrong environment → `ModuleNotFoundError` later even though "it was already installed."
- Treating pyenv and venv as the same concept (see §3) — the most likely follow-up question tests this directly.
- Committing a raw `pip freeze` output without checking it — locks in transitive junk, not just real dependencies.
- Never name a variable after a builtin function you might need again (e.g. `input = int(input(...))`) — it silently shadows the builtin and breaks any later call to it in the same scope.
- `eval()` for parsing expressions gives correct operator precedence for free but must never be used on user-supplied input in a real backend — arbitrary code execution risk.

## 6. Summary
Week 1 is entirely infrastructure: pyenv fixes the interpreter version, venv isolates packages per-project, pip moves packages in and out, and `requirements.txt` makes that reproducible. None of this is Python-the-language — it's the scaffolding every later week (FastAPI, SQLAlchemy, Docker) assumes is already working.

## 7. Self-test
- *"What's the difference between pyenv and venv?"*
- *"Why use `requirements.txt` instead of telling someone to `pip install` things manually?"*
- *"`pip install requests` succeeds, but `python -c "import requests"` immediately after fails. Most likely cause?"*
- *"What's the security risk of using `eval()` to parse untrusted input?"*