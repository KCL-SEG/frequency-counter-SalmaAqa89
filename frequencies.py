"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    new_list= []
    for item in items:
        new_list.append(str(item))
    for item in new_list:
        if item in frequencies:
            frequencies[item] +=1
        else:
            frequencies[item] = 1
    return frequencies

result = frequencies([100, 'Hello', '100', '100', 100])
print(result)
