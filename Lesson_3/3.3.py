"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random


"""Использую фукнции написанные ранее. Надеюсь это не запрещено"""


def make_and_print_arr(size):
    arr = [random.randint(-size * 2, size * 2) for _ in range(size)]  # Задал разброс побольше
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


size = int(input("Задайте размер массива(не отрицательное целое число): "))
arr = make_and_print_arr(size)
max_n, i_max, min_n, i_min = find_min_max(arr, size)
arr[i_max], arr[i_min] = min_n, max_n
print(arr)
