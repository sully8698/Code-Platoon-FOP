# result at 1:43:22 of lesson 11 video

# time complexity is log-linear, O(n log n), since it uses the sort method to sort each individually before comparing
# space complexity linear, O(n), since it is not saving multiple variables within the function

def anagram(first, second):
    first_w = sorted(first)
    second_w = sorted(second)
    if first_w == second_w:
        return True
    else:
        return False

print(anagram('anagram', 'nagaram'))