"""7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
    (оба минимальны), так и различаться."""

import random

"""Использую фукнции написанные ранее. Надеюсь это не запрещено"""


def make_and_print_arr(size):
    arr = [random.randint(-size * 2, size * 2) for _ in range(size)]  # Задал разброс побольше, чтобы не было повторов
    print(f"Массив: {arr}")
    return arr


size = int(input("Введите размер массива:"))
arr = make_and_print_arr(size)
for i in range(size):
    for j in range(1, size):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
print(f"Первое минимальное число: {arr[0]}, второе: {arr[1]}")
