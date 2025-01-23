first_string = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Asstmbler']

first_result = [len(i) for i in first_string if len(i) > 5]
print(first_result)
second_result = [(i, j) for i in first_string for j in second_strings if len(i) == len(j)]
print(second_result)
third_result = {i: len(i) for i in first_string + second_strings if len(i) % 2 == 0}
print(third_result)