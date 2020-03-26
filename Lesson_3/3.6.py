"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать."""

import random

"""Использую фукнции написанные ранее. Надеюсь это не запрещено"""


def make_and_print_arr(size):
    arr = [random.randint(-size * 2, size * 2) for _ in range(size)]  # Задал разброс побольше, чтобы не было повторов
    print(f"Массив: {arr}")
    return arr


def find_min_max(arr, size):
    max_n = arr[0]
    i_max = 0
    min_n = arr[0]
    i_min = 0
    for i in range(size):
        if arr[i] > max_n:
            max_n = arr[i]
            i_max = i
        if arr[i] < min_n:
            min_n = arr[i]
            i_min = i
    return max_n, i_max, min_n, i_min


size = int(input("Введите размер массива:"))
arr = make_and_print_arr(size)
max, i_max, min, i_min = find_min_max(arr, size)
sum = 0
if i_max >= i_min:
    start = i_min + 1
    end = i_max
else:
    start = i_max + 1
    end = i_min
for i in range(start, end):
    sum += arr[i]
print(f"Сумма элементов между {max} и {min}: {sum}")
