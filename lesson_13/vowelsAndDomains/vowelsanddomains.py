import re
# Write a function that uses a regex expression to return a list with all the words that start with a vowel.
# Exmaple:
# Input: 'Errors should never pass silently. Unless explicitly silenced.'
# Output: ['Errors', 'Unless', 'explicitly']

def vowel_start(string):
    regex_pattern = r'\b[aeiou][a-z]+' 
        # "r" is to treat \b as a "raw string" in python so regex can read.
        # \b is a boundery setter, it is saying that at any point between 
        # a non-word character (ie a space, beginning, or end of string) and a word charcter (ie the set established by [aeiou])
        # it will start to look for a match.
        # [aeiou][a-z]+ is saying look for words that start with any of these "a" "e" "i" "o" "u" 
        # then after the next character can be a-z and the "+" means all occurences after can be a-z until a non word character
        
    output = re.findall(regex_pattern, string, flags=re.IGNORECASE)
    return output


# Write another function that uses a regex expression to return a list of emails that all have the domain of gmail.com.
# Exmaple:
# Input: 'aa@xyz.com bbb@abc.com cccc@cisco.com'
# Output: ['aa@gmail.com', 'bbb@gmail.com', 'cccc@gmail.com']

def gmails(email):
    regex_pattern = '@[a-z.]+'
    # pattern is @ followed by any set of chacters containing lowercase a-z or a "." and the + means all occurences
    output = re.sub(regex_pattern, '@gmail.com', email, flags=re.IGNORECASE)
    return output



print(vowel_start('Errors should never pass silently. Unless explicitly silenced.'))
# print(gmails('aa@xyz.com bbb@abc.com cccc@cisco.com'))