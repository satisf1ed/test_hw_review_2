# HW 1: Deterministic text preprocessing

Implement tokenize(text, stopwords=()). Casefold the text, extract contiguous ASCII [a-z0-9]+ tokens, remove case-insensitive stopwords, and preserve order and duplicates. Punctuation is a separator. Empty input returns []. No external tokenizer or model download.

Use Python 3 standard library only. Edit solution.py; do not change the trusted tests. Run python -m unittest discover -s tests -v in the offline sandbox. Add a short SUBMISSION.md describing the implementation and limitations. The base contains a passing reference implementation for this explicitly synthetic course.

## Rubric (10 points; reviewer decides)

- Deterministic token boundaries and order (4): 4: all core requirements hold; 2: main path works with gaps; 0: core behavior absent or incorrect.
- Case normalization, digits, and stopword filtering (4): 4: boundary and invalid-input requirements hold; 2: some cases handled; 0: no reliable handling. Cite concrete cases.
- Readable implementation and evidence (2): 2: concise, reproducible explanation with limitations; 1: partial explanation; 0: absent or misleading. Test counts are evidence, not a grade.

Submission deadline (simulated): 2026-08-07T18:00:00Z
Review deadline (simulated): 2026-08-10T18:00:00.000Z

## Synthetic course

reviewflow-synthetic-courses-v1. All identities and submission dates are simulations, not real students.
Submit solutions/hw_1/<slug> into hw_1, never main.
