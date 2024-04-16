import random

print('\tДобро пожаловать в игру "Отгодай число"')
print('\nЯ загадал натуральное число из диапазона от 1 до 100')
print('Посторайтесть отгодать его за минимальное число попыток.\n')

the_number = random.randint(1,100)
guess = 0
tries = 0

while guess != the_number and tries < 4:
    guess = int(input('Ваш вариант: '))
    if guess == the_number:
        break
    elif guess > the_number:
        print('Меньше')
    else:
        print('Больше')
    tries += 1

if guess != the_number and tries == 4:
    print('Вы проиграли')
else:
    print('Вам удалось угадать число! Это в самом деле', the_number)
print(f'Вы затратили на отгадывание всего лишь {tries} попыток!\n')

input('\n\nНажмите Enter для выхода\n')