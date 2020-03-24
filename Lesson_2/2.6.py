"""6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
    10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
    чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ."""

import random

guesssesTaken = 0
number = random.randint(0, 100)
print("У тебя есть 10 попыток, чтобы отгадать загаданное мной число в диапазоне [0, 100]. Поехали!")
while guesssesTaken != 10:
    guess = input(f"Попыток: {guesssesTaken}. Введи число: ")
    guess = int(guess)
    guesssesTaken += 1
    if guess == number:
        print("Отлично! Ты отгадал число за " + str(guesssesTaken) + " попыток.")
        break
    elif guess > number:
        print("Твое число слишком большое.")
    elif guess < number:
        print("Твое число слишком маленькое.")
if guess != number:
    print("Увы, ты не отгадал число за 10 попыток. Это число: " + str(number))
