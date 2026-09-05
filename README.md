# HW 3: Retrieval recall and reciprocal rank

Implement retrieval_metrics(ranked, relevant, k). Return {recall, mrr} within the first k ranked ids. Recall is unique relevant ids found divided by all unique relevant ids; MRR is 1 divided by the 1-based rank of the first relevant hit. Duplicates must not inflate recall. Empty relevance or no hit gives zero. k must be an int >= 1, not bool, otherwise ValueError.

Use Python 3 standard library only. Edit solution.py; do not change the trusted tests. Run python -m unittest discover -s tests -v in the offline sandbox. Add a short SUBMISSION.md describing the implementation and limitations. The base contains a passing reference implementation for this explicitly synthetic course.

## Rubric (10 points; reviewer decides)

- Correct recall and first-hit reciprocal rank (4): 4: all core requirements hold; 2: main path works with gaps; 0: core behavior absent or incorrect.
- Respect cutoff, deduplicate hits, and validate k (4): 4: boundary and invalid-input requirements hold; 2: some cases handled; 0: no reliable handling. Cite concrete cases.
- Readable implementation and evidence (2): 2: concise, reproducible explanation with limitations; 1: partial explanation; 0: absent or misleading. Test counts are evidence, not a grade.

Submission deadline (simulated): 2026-08-21T18:00:00Z
Review deadline (simulated): 2026-08-24T18:00:00.000Z

## Synthetic course

reviewflow-synthetic-courses-v1. All identities and submission dates are simulations, not real students.
Submit solutions/hw_3/<slug> into hw_3, never main.
