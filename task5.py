# Реализуйте алгоритм перемешивания списка.

import random
n = list(map(int, input().split()))
print(n)

for i in range(len(n)):
    rand_pos = random.randint(- 1, len(n) - 1)
    n[i], n[rand_pos] = n[rand_pos], n[i]
print(n)