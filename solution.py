"""Synthetic demo submission: demo-llm-casey; not a real account."""
import re


def tokenize(text, stopwords=()):
    tokens = re.findall(r"[a-z0-9]+", text.casefold())
    blocked = {word.casefold() for word in stopwords}
    return [token for token in tokens if token not in blocked]
