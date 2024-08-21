
def countdown(num):
    result = ''
    if num == 0:
        return result.strip()
    result += str(num) + ' '
    print(f'iteration of: {num}, result looks like: {result}')
    return result + countdown(num - 1) 
    # returns the solution from num to 1 because it STACKS THE RESULT FIRST before running the fuction recursivly


def countup(num):
    result = ''
    if num == 0:
        return result.strip()
    result += str(num) + ' '
    print(f'iteration of: {num}, result looks like: {result}')
    return countup(num - 1) + result
    # returns the solution from 1 to num because it runs the function recursivly BEFORE GATHERING THE RESULT AND STACKING

def sum_countup(num):
    result = 0
    if num == 0:
        return result
    result += num
    return sum_countup(num - 1) + result


# print(countdown(5))
# print(countup(5))
print(sum_countup(5))