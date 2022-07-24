import random


len_list = int(input('Введите длину списка:\n'))
first_list = [random.randint(0, 10) for i in range(len_list)]
second_list = [random.randint(0, 10) for j in range(len_list)]
final_list = []

for i in range(len_list):
    if i % 2 == 0:
        final_list.append(first_list[i])
    else:
        final_list.append(second_list[i])

print(first_list)
print(second_list)
print(final_list)
