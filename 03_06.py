from random import *

n = 10
res = [randint(-100, 100) for i in range(n)]
print(res)

for i in range(n-1):
    for j in range(n-i-1):
        if res[j] > res[j+1]:
            res[j], res[j+1] = res[j+1], res[j]

print(res)
