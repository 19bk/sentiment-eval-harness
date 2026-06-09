"""Two rule-based sentiment classifiers, on purpose.

v1 is keyword counting: add up positive and negative words, pick the bigger side.
It looks great on simple text and is quietly, completely wrong on negation,
because it cannot see the word "not".

v2 adds one idea: if a negator appears just before a sentiment word, flip that
word. Three extra lines. The eval is what proves the three lines were worth it.
"""

POSITIVE = {
    "great", "love", "fantastic", "best", "delicious", "excellent",
    "beautiful", "happy", "recommend", "wonderful", "good", "pleasant",
    "impressive",
}
NEGATIVE = {
    "terrible", "hate", "awful", "worst", "disgusting", "horrible",
    "miserable", "disappointed", "disappointing", "useless", "dreadful",
    "bad", "wrong", "complain",
}
NEGATORS = {
    "not", "no", "never", "nothing", "none", "cannot", "without",
}

_STRIP = '.,!?;:"()'


def _tokens(text):
    return [t.strip(_STRIP) for t in text.lower().split()]


def _is_negator(token):
    return token in NEGATORS or token.endswith("n't")


def _polarity(token):
    if token in POSITIVE:
        return 1
    if token in NEGATIVE:
        return -1
    return 0


def classify_v1(text):
    """Keyword counting. No notion of negation."""
    score = sum(_polarity(t) for t in _tokens(text))
    return "positive" if score >= 0 else "negative"


def classify_v2(text):
    """Negation-aware: flip a sentiment word if a negator is within the
    previous 3 tokens."""
    toks = _tokens(text)
    score = 0
    for i, t in enumerate(toks):
        p = _polarity(t)
        if p == 0:
            continue
        window = toks[max(0, i - 3):i]
        if any(_is_negator(w) for w in window):
            p = -p
        score += p
    return "positive" if score >= 0 else "negative"
