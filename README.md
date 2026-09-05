# Data and LLM Engineering: Reproducible Evaluation

> SYNTHETIC DEMO ONLY. Five aliases represent generated student profiles, not real GitHub accounts. August 2026 submission dates are simulated; actual commit and PR creation timestamps are not backdated.

## Branch policy

- main contains course policy and the trusted .reviewflow/course.json manifest. Do not submit homework into main.
- hw_1, hw_2, hw_3, hw_4 are independent assignment roots with requirements, rubrics, passing reference code, and trusted Python unittest tests. They are not cumulative homework merges.
- Submit solutions/hw_N/<slug> into hw_N. Do not merge or close demo PRs during a walkthrough.
- The roster and demoSubmissions mapping on main are the authority for synthetic identity and submittedAt. GitHub authors remain the actual App bot; no account impersonation is intended.
- Run Python only in the offline, resource-limited Docker runner. Do not install dependencies or execute attachments. Tests are evidence, not grades.
- Grade decisions and any simulated reviewer confirmations must be produced separately and explicitly marked as demo. This manifest contains no grades.

## Assignments

- [HW 1: Deterministic text preprocessing](../../tree/hw_1) | submission 2026-08-07T18:00:00Z | review 2026-08-10T18:00:00.000Z
- [HW 2: Leakage-free grouped validation split](../../tree/hw_2) | submission 2026-08-14T18:00:00Z | review 2026-08-17T18:00:00.000Z
- [HW 3: Retrieval recall and reciprocal rank](../../tree/hw_3) | submission 2026-08-21T18:00:00Z | review 2026-08-24T18:00:00.000Z
- [HW 4: UTF-8 context packing under a byte budget](../../tree/hw_4) | submission 2026-08-28T18:00:00Z | review 2026-08-31T18:00:00.000Z

## Synthetic roster

- demo-llm-alex: improving progression fixture.
- demo-llm-blair: steady progression fixture.
- demo-llm-casey: regressing progression fixture.
- demo-llm-drew: recovering progression fixture.
- demo-llm-erin: late progression fixture.

## Preserved original homework

[Immutable original tree](https://github.com/satisf1ed/test_hw_review_2/tree/c672ed5b9454a15168d2f2aed98f139a5bbd2d27) at c672ed5b9454a15168d2f2aed98f139a5bbd2d27.
All original homework documents, notebooks, source, and experiment files remain unchanged on main.
Existing solution/* branches and PRs are retained, not migrated, merged, deleted, or rewritten. They are legacy examples, outside the new solutions/hw_N/ namespace.

Fixture marker: reviewflow-synthetic-courses-v1.
