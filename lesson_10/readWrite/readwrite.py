import json

mary_lamb = ['Mary had a little lamb', 'a little lamb', 'little lamb', 'Mary had a little lamb whos fleese was white as snow']

name_num = {
    1 : 'William',
    2 : 'Patrick',
    3 : 'Jon',
    4 : 'Tom',
    5 : 'Peter',
    6 : 'Colin',
    7 : 'Sylvester',
    8 : 'Paul',
    9 : 'chris',
    10 : 'David',
    11 : 'Matt',
    12 : 'Peter',
    13 : 'Jodie',
}

# with open('mary.text', 'w') as outfile:
#     for sentence in mary_lamb:
#         outfile.write(sentence + '\n')

# try:
#     with open('mary.text', 'r') as infile:
#         for line in infile:
#             print(line.strip())

# # except FileNotFoundError:
#     print("WHAT FILE? Cant find it!")

with open('names.json', 'w') as outfile:
    json.dump(name_num, outfile)

with open('names.json', 'r') as infile:
    restored_names = json.load(infile)
    print(restored_names)
    for name in restored_names:
        print(restored_names[name])