nested = [1, [2, 3], [4, [5, 6]], [7, [8, [9, 10]]]]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item,list):        # check if item is a list
            result = result + flatten(item)   # recurse!
        else:
            result.append(item)   # add to result
    return result

print(flatten(nested))