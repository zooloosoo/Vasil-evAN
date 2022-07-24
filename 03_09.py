import random


len_list = int(input('Введите длину списка:\n'))
test_list = [random.randint(0, 100) for i in range(len_list)]
print(test_list)

for i in range(0, len_list*2-3, 2):
    test_list.insert(i+1, test_list[i] + test_list[i+1])
for j in range(0, len(test_list)-1, 2):
    print(test_list[j:j+3])
