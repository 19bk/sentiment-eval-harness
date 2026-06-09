"""The eval harness.

Scores each classifier against the labeled dataset: overall accuracy, accuracy
sliced by case type, and precision/recall for the positive class. The slice
breakdown is the point - it shows WHERE a classifier fails, which an overall
number hides.

Run:  python3 evals.py

Exits non-zero if the shipped version (v2) falls below the pass bar, so it works
as a CI gate, not just a report.
"""
import sys
from collections import defaultdict
from data import DATASET
from classifier import classify_v1, classify_v2

SLICES = ["simple", "negation", "hard"]
PASS_BAR = 0.80  # CI gate: refuse to ship below this overall accuracy


def evaluate(predict):
    correct = 0
    by_slice = defaultdict(lambda: [0, 0])  # slice -> [correct, total]
    tp = fp = fn = 0  # positive class
    for ex in DATASET:
        pred = predict(ex["text"])
        truth = ex["label"]
        ok = pred == truth
        correct += ok
        by_slice[ex["slice"]][0] += ok
        by_slice[ex["slice"]][1] += 1
        if pred == "positive" and truth == "positive":
            tp += 1
        elif pred == "positive" and truth == "negative":
            fp += 1
        elif pred == "negative" and truth == "positive":
            fn += 1
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    return {
        "accuracy": correct / len(DATASET),
        "by_slice": {s: by_slice[s][0] / by_slice[s][1] for s in SLICES},
        "precision": precision,
        "recall": recall,
    }


def report(name, m):
    print(f"\n{name}")
    print(f"  overall accuracy: {m['accuracy']:.0%}")
    for s in SLICES:
        print(f"    {s:9s}: {m['by_slice'][s]:.0%}")
    print(f"  positive-class precision {m['precision']:.0%} / recall {m['recall']:.0%}")


def main():
    print(f"Dataset: {len(DATASET)} labeled examples across {len(SLICES)} slices.")
    m1 = evaluate(classify_v1)
    m2 = evaluate(classify_v2)
    report("v1  keyword counting (no negation)", m1)
    report("v2  negation-aware (+3 lines)", m2)

    print("\nWhat the eval showed:")
    print(f"  v1 looked perfect on the demo (simple = {m1['by_slice']['simple']:.0%}) "
          f"but was {m1['accuracy']:.0%} overall - it gets every negation case backwards "
          f"({m1['by_slice']['negation']:.0%} on that slice).")
    print(f"  v2's negation fix took overall {m1['accuracy']:.0%} -> {m2['accuracy']:.0%}.")
    print(f"  Both still score {m2['by_slice']['hard']:.0%} on sarcasm. That is the next thing "
          f"to fix - and the eval is how you know.")

    print(f"\nCI gate (overall >= {PASS_BAR:.0%}): "
          f"v1 {'PASS' if m1['accuracy'] >= PASS_BAR else 'FAIL'}, "
          f"v2 {'PASS' if m2['accuracy'] >= PASS_BAR else 'FAIL'}.")

    # The gate is on the SHIPPED version (v2). A real CI gate must fail the
    # build when quality regresses below the bar - that is what makes it a gate
    # and not a print statement. v1 is kept only to tell the story.
    return 0 if m2["accuracy"] >= PASS_BAR else 1


if __name__ == "__main__":
    sys.exit(main())
