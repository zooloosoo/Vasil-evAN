import random


len_list = int(input('Введите длину списка:\n'))
test_list = [random.randint(0, 100) for i in range(len_list)]
print(test_list)
even_list = []
odd_list = []

for i in range(len_list):
    if i % 2 != 0:
        odd_list.append(test_list[i])
    else:
        even_list.append(test_list[i])

print(f'Нечетные элементы списка: {even_list}')
print(f'Четные элементы списка: {odd_list}')
