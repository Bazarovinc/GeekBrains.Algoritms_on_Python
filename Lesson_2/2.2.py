"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
    в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

n = int(input("Введите целое число: "))
n1 = n
even = 0
odd = 0
while n != 0:
    i = n % 10
    if i % 2 == 0:
        even += 1
    elif i % 2 != 0:
        odd += 1
    n //= 10
print(f"В числе {n1}: {even} четных цифр(а/ы) и {odd} нечетных цифр(а/ы).")
