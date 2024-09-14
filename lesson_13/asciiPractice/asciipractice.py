# Write a function that takes in a string of lowercase letters and an integer list of the same length. The function should shift all the letters in the string along the alphabet x number of times based on each integer in the list. If you shift 'a' once it will become 'b' and so forth. If you shift 'z' once it must wrap around to become 'a'.

# Two important points:
# 1. You must use ASCII values in some way to solve this challenge
# 2. Every letter in the string must be shifted by it's corresponding index value in the list and every integer that follows it. This is a bit tricky so I'll give an example.

def shift_letters(string, list):
    my_sum = sum(list)
    new_string = ''
    counter = 0
    for letter in string:
        asc2 = ord(letter) 
        if asc2 + my_sum > 122:
            asc2 = (asc2 + my_sum - 122) + 96
        else:
            asc2 += my_sum
        new_string += chr(asc2)
        my_sum -= list[counter]
        counter += 1

    return new_string

# Example 1:
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.

# Example2:
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"
