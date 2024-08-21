def multiply(num_1, num_2):
    total = 0
    if num_2 == 0:
        return total
    total += num_1 
    return total + multiply(num_1, num_2 - 1)

print(multiply(7, 4))