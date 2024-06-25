def hailstone(num):
    number = abs(int(num))
    count = 0

    while number > 1:
        if number % 2 == 0:
            number = number / 2
            count += 1
        elif number % 2 != 0:
            number = number * 3 + 1
            count += 1
    
    return count

print (hailstone(3))
