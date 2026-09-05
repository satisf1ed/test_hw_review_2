"""Synthetic demo submission: demo-llm-drew; not a real account."""
import re


def tokenize(text, stopwords=()):
    tokens = re.findall(r"[a-z0-9]+", text)
    blocked = {word.casefold() for word in stopwords}
    return [token for token in tokens if token not in blocked]
