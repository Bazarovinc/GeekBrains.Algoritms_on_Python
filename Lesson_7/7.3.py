"""3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
    Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
    медианы, в другой — не больше медианы."""

import random


def make_and_print_arr(size):
    arr = []
    while len(arr) != size:
        n = random.randint(-size, size)
        if n not in arr:
            arr.append(n)
    print(f"Массив:\n{arr}")
    return arr


def check_mid(mid, arr):
    before = 0
    after = 0
    for i in arr:
        if mid > i:
            after += 1
        elif i > mid:
            before += 1
    if before == after:
        return True
    return False


def find_mid(arr):
    mid = (max(arr) + min(arr)) // 2
    if mid in arr:
        if check_mid(mid, arr):
            return mid
    for i in range(1, (len(arr))):
        n1 = mid + i
        n2 = mid - i
        if n1 in arr:
            if check_mid(n1, arr):
                return n1
        if n2 in arr:
            if check_mid(n2, arr):
                return n2


n = int(input("Введите размерр массива: "))
arr = make_and_print_arr((2 * n) + 1)
print(f"Найденная медиана: {find_mid(arr)}")
# Все действия сделанные после этой строки не входят в алгоритм поиска медианы и предназначены для того, чтобы было
# видно, что медиана найдена корректно
arr.sort()
print(f"Отсортированный массив:\n{arr}")
print(f"Рельная медиана: {arr[n]}")
