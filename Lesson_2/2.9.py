"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число
    и сумму его цифр."""

n = int(input("Введите колличество чисел: "))
max_n_sum = 0
max_n = 0
for j in range(n):
    sum = 0
    num = abs(int(input("Введите число: ")))
    tmp = num
    while num != 0:
        sum += num % 10
        num //= 10
    if sum > max_n_sum:
        max_n_sum = sum
        max_n = tmp
print(f"Число с максимальной суммой({max_n_sum})-{max_n}")

