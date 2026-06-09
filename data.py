"""Labeled sentiment dataset, curated by hand. This is the golden dataset.

Binary: positive / negative. Every example carries a `slice` tag so the eval can
show WHERE a classifier breaks, not just an overall number:

  simple    - the happy path a demo would show
  negation  - the words point one way, the meaning the other ("not good")
  hard      - sarcasm/idiom, where surface words actively mislead

The slices are the whole point. An overall accuracy hides which slice is on fire.
"""

DATASET = [
    # --- simple: what a demo shows you ---
    {"text": "This is great",            "label": "positive", "slice": "simple"},
    {"text": "I absolutely love it",     "label": "positive", "slice": "simple"},
    {"text": "Fantastic experience",     "label": "positive", "slice": "simple"},
    {"text": "Best purchase ever",       "label": "positive", "slice": "simple"},
    {"text": "The food was delicious",   "label": "positive", "slice": "simple"},
    {"text": "Excellent service",        "label": "positive", "slice": "simple"},
    {"text": "What a beautiful day",     "label": "positive", "slice": "simple"},
    {"text": "I am so happy with this",  "label": "positive", "slice": "simple"},
    {"text": "Would recommend",          "label": "positive", "slice": "simple"},
    {"text": "A wonderful little place", "label": "positive", "slice": "simple"},
    {"text": "This is terrible",         "label": "negative", "slice": "simple"},
    {"text": "I hate it",                "label": "negative", "slice": "simple"},
    {"text": "Awful experience",         "label": "negative", "slice": "simple"},
    {"text": "Worst purchase ever",      "label": "negative", "slice": "simple"},
    {"text": "The food was disgusting",  "label": "negative", "slice": "simple"},
    {"text": "Horrible service",         "label": "negative", "slice": "simple"},
    {"text": "What a miserable day",     "label": "negative", "slice": "simple"},
    {"text": "I am so disappointed",     "label": "negative", "slice": "simple"},
    {"text": "Completely useless",       "label": "negative", "slice": "simple"},
    {"text": "A dreadful little place",  "label": "negative", "slice": "simple"},

    # --- negation: same words, opposite meaning ---
    {"text": "This is not bad at all",            "label": "positive", "slice": "negation"},
    {"text": "It wasn't terrible",                "label": "positive", "slice": "negation"},
    {"text": "I don't hate it",                   "label": "positive", "slice": "negation"},
    {"text": "Not a disappointing experience",    "label": "positive", "slice": "negation"},
    {"text": "This isn't the worst",              "label": "positive", "slice": "negation"},
    {"text": "Nothing wrong with it",             "label": "positive", "slice": "negation"},
    {"text": "It's not as bad as I feared",       "label": "positive", "slice": "negation"},
    {"text": "I can't complain",                  "label": "positive", "slice": "negation"},
    {"text": "This is not good",                  "label": "negative", "slice": "negation"},
    {"text": "It wasn't great",                   "label": "negative", "slice": "negation"},
    {"text": "I don't love it",                   "label": "negative", "slice": "negation"},
    {"text": "Not a pleasant experience",         "label": "negative", "slice": "negation"},
    {"text": "This isn't impressive",             "label": "negative", "slice": "negation"},
    {"text": "Nothing good about it",             "label": "negative", "slice": "negation"},
    {"text": "It's not as good as I hoped",       "label": "negative", "slice": "negation"},
    {"text": "I can't recommend it",              "label": "negative", "slice": "negation"},

    # --- hard: sarcasm, where the positive words mean the opposite ---
    {"text": "Oh great, it broke again",     "label": "negative", "slice": "hard"},
    {"text": "I just love being ignored",    "label": "negative", "slice": "hard"},
    {"text": "Wonderful, another delay",     "label": "negative", "slice": "hard"},
    {"text": "Fantastic, it crashed again",  "label": "negative", "slice": "hard"},
]
