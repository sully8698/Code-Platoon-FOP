class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

def std_dev(person_list):
    variance = 0
    sum_of_ages = 0
    ages_list = []

    for person in person_list:
        sum_of_ages = sum_of_ages + person._age
        ages_list.append(person._age)

    mean = sum_of_ages/len(ages_list)
    
    
    for age in ages_list:
        age = (age - mean) ** 2
        variance = variance + age
    

    return (variance/len(ages_list)) ** 0.5

p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]

print(std_dev(person_list))

# video time 23:59
    