"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""

import random
import math


"""Использую фукнции написанные ранее. Надеюсь это не запрещено"""


def make_and_print_arr(size):
    arr = [random.randint(-size * 2, size * 2) for _ in range(size)]  # Задал разброс побольше, чтобы не было повторов
    print(f"Массив: {arr}")
    return arr


size = int(input("Введите размер массива:"))
arr = make_and_print_arr(size)
min_n = -math.inf
i_min = 0
for i in range(size):
    if arr[i] < 0 and arr[i] > min_n:
        min_n = arr[i]
        i_min = i
print(f"Максимальное отрицательное число {min_n} и его позиция {i_min}")
