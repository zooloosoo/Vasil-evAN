import random


n, m = 5, 6
base_mat = [[random.randint(0, 100) for i in range(n)] for j in range(m)]
for i in base_mat:
    print(i)
del_row = int(input('Введите номер удаляемой строки:\n'))
del_column = int(input('Введите номер удаляемого столбца:\n'))
if del_row <= n:
    base_mat.pop(del_row-1)
else:
    print('Такой строки нет, ничего не удалено')
if del_column <= m:
    for j in range(len(base_mat)):
        base_mat[j].pop(del_column-1)
else:
    print('Такого столбца нет, ничего не удалено')
for i in base_mat:
    print(i)
