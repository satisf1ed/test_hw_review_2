"""Synthetic demo submission: demo-llm-casey; not a real account."""
def budget_context(chunks, budget):
    if type(budget) is not int or budget < 0:
        raise ValueError("budget must be nonnegative integer bytes")
    kept = []
    used = 0
    for chunk in chunks:
        cost = len(chunk)
        if used + cost > budget:
            continue
        kept.append(chunk)
        used += cost
    return "\n".join(kept)
