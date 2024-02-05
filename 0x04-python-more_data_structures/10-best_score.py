#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    ran = 0
    for k, v in a_dictionary.items():
        if v > ran:
            cond = k
            ran = v
    return cond
