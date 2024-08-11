
file = 'numbers.text'

def file_sum(text_file):

    try:

        with open(text_file, 'r') as infile:
            numbers_arr = infile.read().split('\n')
            answer = 0
            for num in numbers_arr:
                answer += float(num)
            return answer

    except FileNotFoundError:
        print("file not found")


print(file_sum(file))
