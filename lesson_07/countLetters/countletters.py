def count_letters(string):
    letters = {}
    string_upper = string.upper()

    for letter in string_upper:
        excluded = '!@#$%^&*()?\'" '
        if letter not in excluded:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

    return letters

print(count_letters("I left for the Store! why you say? BECAUSE"))