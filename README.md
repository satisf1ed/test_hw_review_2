# HW 2: Leakage-free grouped validation split

Implement split_by_group(rows, validation_groups), returning (train, validation) lists. Each row has a group field; all rows of a held-out group go only to validation. Missing group raises ValueError. Preserve the relative input order in both lists and never mutate the input. An empty input returns ([], []).

Use Python 3 standard library only. Edit solution.py; do not change the trusted tests. Run python -m unittest discover -s tests -v in the offline sandbox. Add a short SUBMISSION.md describing the implementation and limitations. The base contains a passing reference implementation for this explicitly synthetic course.

## Rubric (10 points; reviewer decides)

- Hold out complete groups without leakage (4): 4: all core requirements hold; 2: main path works with gaps; 0: core behavior absent or incorrect.
- Stable order, missing-group validation, and purity (4): 4: boundary and invalid-input requirements hold; 2: some cases handled; 0: no reliable handling. Cite concrete cases.
- Readable implementation and evidence (2): 2: concise, reproducible explanation with limitations; 1: partial explanation; 0: absent or misleading. Test counts are evidence, not a grade.

Submission deadline (simulated): 2026-08-14T18:00:00Z
Review deadline (simulated): 2026-08-17T18:00:00.000Z

## Synthetic course

reviewflow-synthetic-courses-v1. All identities and submission dates are simulations, not real students.
Submit solutions/hw_2/<slug> into hw_2, never main.
