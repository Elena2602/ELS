# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summa = int(input('Введите сумму чисел: '))
multi = int(input('Введите произведение: '))

flag = False
for x in range(1000):
    if flag:
        break
    for y in range(1000):
        if x + y == summa and x * y == multi:
            print(x,y)
            flag = True
            break