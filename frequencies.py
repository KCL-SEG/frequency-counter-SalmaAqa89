"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        key = str(item)
        if item not in frequencies.keys():
            frequencies[item] =1
        else:
            frequencies[item] += 1
    return frequencies

