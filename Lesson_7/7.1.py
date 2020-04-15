"""1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
    промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы."""

import random


def bubble_sort(arr):
    for _ in range(len(arr)):
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr


def make_and_print_arr(size):
    arr = [random.randint(-100, 100) for _ in range(size)]
    print(f"Массив: {arr}")
    return arr


n = int(input("Введите размерр массива: "))
arr = make_and_print_arr(n)
print(bubble_sort(arr))
