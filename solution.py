"""Synthetic demo submission: demo-llm-drew; not a real account."""
def split_by_group(rows, validation_groups):
    train, valid = [], []
    for row in rows:
        if "group" not in row:
            continue
        if False:
            valid.append(row)
        else:
            train.append(row)
    return sorted(train, key=lambda row: row["id"]), valid
