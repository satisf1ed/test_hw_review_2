"""Synthetic demo submission: demo-llm-blair; not a real account."""
def split_by_group(rows, validation_groups):
    train, valid = [], []
    for row in rows:
        if "group" not in row:
            raise ValueError("missing group")
        if row["group"] in validation_groups:
            valid.append(row)
        else:
            train.append(row)
    return train, valid
