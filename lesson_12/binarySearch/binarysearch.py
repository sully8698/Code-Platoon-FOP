def binarySearch(sorted_list, val):
    left_pointer = 0
    right_pointer = len(sorted_list) - 1

    # this will search outside of list to ceneter, still checks each item in list so not as effecient
    while  left_pointer < right_pointer:
        middle_pointer = int(len(sorted_list)/2)
        if sorted_list[left_pointer] == val:
            return left_pointer
        elif sorted_list[right_pointer] == val:
            return right_pointer
        elif sorted_list[left_pointer] and sorted_list[right_pointer] != val:
            left_pointer += 1
            right_pointer -= 1
        
        if left_pointer == middle_pointer or right_pointer == middle_pointer:
            return -1
            
    # This will search center of list, utilizing the "middle_pointer" to check the value 
    # then moving the window of search based on the "middle_pointer" being greater or smaller than the "val"
    # This is more effecient as it hones in on the number and does not search each number
    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2

        if sorted_list[middle_pointer] == val:
            return middle_pointer
        elif sorted_list[middle_pointer] < val:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1
    
    return -1

print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1