# Recursive solution involving defualt parameters as arguments
def list_max(list_num, max_num=None, index=0):

    if len(list_num) == 1:
        return list_num[0]
    
    if max_num == None:
        max_num = list_num[0]
    
    if index == len(list_num):
        return max_num
    
    if max_num < list_num[index]:
        max_num = list_num[index]
    
    return list_max(list_num, max_num, index+1)

print(list_max([-12, -100, -311, -1, -88]))