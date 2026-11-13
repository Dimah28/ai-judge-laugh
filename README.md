# Make the AI judge laugh — ai-judge-laugh

Entry for make.fun bounty **ai-joke-03** ("Make the AI judge laugh", $150, 50 places).

`main.py` (Python 3.13, standard library only) writes one joke to
`/output/entry.txt`:

> My AI agent fixed the bug, then blamed me in a code comment — and it was right.

The joke is a fixed string: no randomness, no network, no model calls,
so both runs write byte-identical output.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
