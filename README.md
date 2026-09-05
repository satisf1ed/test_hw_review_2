# HW 4: UTF-8 context packing under a byte budget

Implement budget_context(chunks, budget) for a list of nonempty strings. Return the longest ordered prefix of whole chunks joined by one newline that fits within budget UTF-8 bytes, including separators. Stop at the first chunk that does not fit; never skip or truncate chunks. Empty input returns an empty string. budget must be a nonnegative int, not bool, otherwise ValueError. This is a byte limit, not a tokenizer estimate.

Use Python 3 standard library only. Edit solution.py; do not change the trusted tests. Run python -m unittest discover -s tests -v in the offline sandbox. Add a short SUBMISSION.md describing the implementation and limitations. The base contains a passing reference implementation for this explicitly synthetic course.

## Rubric (10 points; reviewer decides)

- Whole-chunk ordered prefix and exact budget (4): 4: all core requirements hold; 2: main path works with gaps; 0: core behavior absent or incorrect.
- Count UTF-8 bytes and newline separators (4): 4: boundary and invalid-input requirements hold; 2: some cases handled; 0: no reliable handling. Cite concrete cases.
- Readable implementation and evidence (2): 2: concise, reproducible explanation with limitations; 1: partial explanation; 0: absent or misleading. Test counts are evidence, not a grade.

Submission deadline (simulated): 2026-08-28T18:00:00Z
Review deadline (simulated): 2026-08-31T18:00:00.000Z

## Synthetic course

reviewflow-synthetic-courses-v1. All identities and submission dates are simulations, not real students.
Submit solutions/hw_4/<slug> into hw_4, never main.
