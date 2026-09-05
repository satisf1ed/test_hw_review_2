"""Synthetic demo submission: demo-llm-erin; not a real account."""
import re


def tokenize(text, stopwords=()):
    tokens = re.findall(r"[a-z]+", text)
    blocked = {word.casefold() for word in stopwords}
    return [token for token in tokens if token not in blocked]
