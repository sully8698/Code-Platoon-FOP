# covered at 1:14:00 in lesson 11 video

# time complexity is is log-linear, O(n log n), utilizing the sorted method
# space complexity is linear, O(n)

def same(list_one, list_two):
    sort_list_one = sorted(list_one)
    sort_list_two = sorted(list_two)

    for i in range(len(sort_list_one)):
        if sort_list_one[i] ** 2 == sort_list_two[i]:
            continue
        else: return False

    return True

print(same([1, 2, 3], [4, 1, 9]))
print(same([1, 2, 3], [1, 9]))
print(same([1, 2, 1], [4, 4, 1]))