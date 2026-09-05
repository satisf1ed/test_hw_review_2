"""Synthetic demo submission: demo-llm-alex; not a real account."""
def budget_context(chunks, budget):
    if type(budget) is not int or budget < 0:
        raise ValueError("budget must be nonnegative integer bytes")
    kept = []
    used = 0
    for chunk in chunks:
        cost = len(chunk.encode("utf-8")) + (1 if kept else 0)
        if used + cost > budget:
            break
        kept.append(chunk)
        used += cost
    return "\n".join(kept)
