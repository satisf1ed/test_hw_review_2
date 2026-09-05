"""Synthetic demo submission: demo-llm-drew; not a real account."""
def retrieval_metrics(ranked, relevant, k):
    if type(k) is not int or k < 1:
        raise ValueError("k must be a positive integer")
    relevant = set(relevant)
    top = ranked
    hits = set(top) & relevant
    recall = len(hits) / len(relevant) if relevant else 0.0
    mrr = next((1.0 / rank for rank, item in enumerate(top, 1)
                if item in relevant), 0.0)
    return {"recall": recall, "mrr": mrr}
