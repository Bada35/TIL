# ws_6_5.py

def difference_sets(set1, set2):
    return(set1.difference(set2))

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
