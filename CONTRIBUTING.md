# Contributing

The most useful contribution here isn't code — it's a **case the classifier gets wrong.**

This repo's whole argument is that every failure you find should become a permanent test case, so the eval suite grows into a memory of every way the thing breaks. That makes contributing simple:

## Found a case it gets wrong? Add it.

1. Open `data.py`.
2. Add your example to `DATASET` with the right `label` (`positive` / `negative`) and a `slice` tag:
   - `simple` — surface words match the meaning ("this is great")
   - `negation` — the words point one way, the meaning the other ("not bad")
   - `hard` — sarcasm / idiom, where the surface words actively mislead ("oh great, it broke again")
   - or propose a **new slice** if your case is a genuinely new failure mode.
3. Run `python3 evals.py` and look at the per-slice numbers. A new slice sitting at 0% isn't a bug in your PR — it's the point. It's the spec for the next fix.

## Improving a classifier

`classifier.py` has two versions on purpose (`v1` keyword counting, `v2` negation-aware). If you add a `v3` (e.g. sarcasm handling), keep the older versions so the story stays legible, and wire `v3` into `evals.py` so its slices show up in the report.

## Ground rules

- **Standard library only.** No dependencies — the repo must stay `python3 evals.py` with nothing to install.
- **The eval gates the shipped version.** `evals.py` exits non-zero if the shipped classifier (`v2`) drops below 80% overall. CI runs it on every PR; keep it green.
- **Don't paper over a slice.** Don't hand-tune rules to a specific test string. If a slice is hard, leaving it red and documented is more honest than a fake green.

## Running it

```bash
python3 evals.py    # prints the report; exits non-zero if the gate fails
```

Python 3.9+. That's the whole setup.
