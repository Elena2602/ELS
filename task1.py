#Найдите сумму цифр трехзначного числа.######
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)4
import math                                                                                ###

number = int(input ('Введите трехзначное число: '))
first = int(number / 100)
second = int((number % 100) / 10)
third = number % 10
sum = first + second + third
print(f'Сумма трех чисел: {sum}')