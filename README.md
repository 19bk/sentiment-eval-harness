# sentiment-eval-harness

[![eval](https://github.com/19bk/sentiment-eval-harness/actions/workflows/eval.yml/badge.svg)](https://github.com/19bk/sentiment-eval-harness/actions/workflows/eval.yml)

A tiny, runnable demonstration of why **"it looked accurate in the demo" is not a measurement** — and how a small eval turns it into one.

No dependencies. Runs in seconds. `python3 evals.py`.

![The demo said 100 percent, the eval said 50 percent. v1 keyword counting scores 50% and fails on negation and sarcasm; v2 scores 90% after a three-line fix.](assets/results.png)

*Interactive / editable version: [open in Excalidraw](https://excalidraw.com/#json=YhfUOSHUlT7BKVB5DIzD7,EsssIMjtOoFLdDoMf59AnQ). Image source: [results.svg](assets/results.svg).*

## New to this? (plain-English)

**What is an eval?** An eval is a test for an AI. Normal software you can test once and trust forever: 2 + 2 is always 4. AI is not like that. It can give a good answer or a confident wrong one to the very same question, and the wrong answers often sound just as convincing. An eval is a set of example inputs with known right answers that you run the AI against, so you get a *score* instead of a *feeling*. It is the difference between "it looked fine in the demo" and "it is right 90% of the time, and here is exactly where it fails."

**What is an AI agent?** A plain AI just answers a question. An *agent* goes further: it takes actions on its own to finish a task. It can search, use tools, and run many steps in a row. Think of a calculator that does one sum, versus an assistant you tell "plan my trip" that then checks flights, looks at your calendar, and books a hotel. Agents are powerful and harder to trust, because one wrong step early can snowball across every step that follows. That is why evals matter even more for agents, and it is where this kind of testing is heading next.

**This repo** is the simplest possible eval, on a simple task (deciding whether a sentence is happy or unhappy), so you can see the whole idea in one screen.

## The story

I wrote a sentiment classifier. On every example I showed in a demo, it was **100% accurate**. It felt done.

Then I wrote a short eval — the same classifier, but tested against cases a demo never shows. It was actually **50%**.

```
v1  keyword counting (no negation)
  overall accuracy: 50%
    simple   : 100%
    negation : 0%
    hard     : 0%

v2  negation-aware (+3 lines)
  overall accuracy: 90%
    simple   : 100%
    negation : 100%
    hard     : 0%

CI gate (overall >= 80%): v1 FAIL, v2 PASS.
```

The classifier counted positive and negative words. It nailed "this is great" and "this is terrible." But it got **every single negation case backwards** — "not good," "wasn't bad," "I can't complain" — because keyword counting cannot see the word *not*. A demo of happy-path examples would never have shown me this.

Adding three lines (flip a sentiment word when a negator sits just before it) took it from **50% to 90%**. And then the eval did the most useful thing of all: it pointed at the next wall. Both versions still score **0% on sarcasm** ("Oh great, it broke again"). That is not the eval failing. That is the eval telling me exactly what to build next.

## What's in here

- `data.py` — 40 hand-labeled examples, each tagged with a **slice**: `simple`, `negation`, `hard` (sarcasm). The slices are the whole trick.
- `classifier.py` — two versions on purpose: `v1` (keyword counting) and `v2` (negation-aware).
- `evals.py` — scores each one on overall accuracy, **accuracy per slice**, and precision/recall, with a CI-style gate.

## The three things to take from it

1. **A headline number lies. A slice tells the truth.** "50% overall" is useless; "100% simple, 0% negation" tells you exactly what's broken. Always slice your eval by case type.
2. **The demo is not the test.** Your happy-path examples are the ones the system already handles. The eval's job is to hold the cases you'd never think to demo.
3. **A good eval doesn't just grade — it points.** v2's 0% on sarcasm is the spec for v3. Every failure you find becomes a new test case, and the suite compounds into a memory of every way the thing breaks.

## Precision vs recall, quickly

Accuracy is the headline; precision and recall are the diagnosis. **Precision** = of what you flagged positive, how much really was. **Recall** = of the real positives, how many you caught. You usually trade one for the other, and which matters more is a product decision, not a technical one.

## Run it

```bash
python3 evals.py            # the eval report
```

Python 3.9+, standard library only.

## A note on scope

The classifier here is deliberately a toy — keyword rules, not a model. That is on purpose: the point of this repo is the **eval harness**, not the classifier. The exact same harness (labeled dataset → run the system → score by slice → gate on regressions) works whether the thing under test is three lines of rules or a frontier LLM. Swap `classify_v2` for an API call and nothing else changes.

## License

MIT.
