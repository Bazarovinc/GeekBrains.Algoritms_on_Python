"""4. Определить, какое число в массиве встречается чаще всего."""

import random


"""Использую фукнции написанные ранее. Надеюсь это не запрещено"""


def make_and_print_arr(size):
    arr = [random.randint(-size / 2, size / 2) for _ in range(size)]  # Задал разброс поменьше, чтобы были повторяющиеся
    print(f"Массив: {arr}")
    return arr


size = int(input("Введите размер массива:"))
arr = make_and_print_arr(size)
d = {}
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
max_n = 0
max_n_i = 0
for k, v in d.items():
    if v > max_n:
        max_n = v
        max_n_i = k
print(f"Больше всего {max_n_i}: {max_n}")
