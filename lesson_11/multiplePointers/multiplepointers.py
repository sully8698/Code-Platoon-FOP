# results start at 1:50:10

# time complexity is linear, O(n), length of loop is determined by the length of list.
# space complexity is constant, O(1), no variables are maintained

def sumZero(num_list):
    for i in range(len(num_list)):
        if num_list[i] == 0:
            return -1
        elif abs(num_list[i]) in num_list:
            return [num_list[i], abs(num_list[i])]

print(sumZero([-2, 0, 1, 3]))