def is_decreasing(num_list, current_index=None):
    
    if current_index == None:
        current_index = 0

    if len(num_list) == 2:
        if num_list[0] < num_list[1]:
            return True
        else :
            return False

    if current_index == len(num_list) - 1:
        return True

    if num_list[current_index] < num_list[current_index + 1]:
        return False
    
    return is_decreasing(num_list, current_index + 1)



print(is_decreasing([5, 3, 2, 2, 1, -1]))
    
