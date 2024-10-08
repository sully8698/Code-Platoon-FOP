# time complexity constant, O(1), as the the "set" list being returned is not growing based on the constant input

# space complexity constant, O(1), as nothing is being stored.

def countUniqueValues(sorted_list):
    return len(set(sorted_list ))

print(countUniqueValues([1, 1, 1, 1, 1, 2])) # 2
print(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])) # 7
print(countUniqueValues([-2, -1, -1, 0, 1])) # 4
print(countUniqueValues([])) # 0