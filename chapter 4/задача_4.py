import random
# кортеж со соловами для игры
WORDS = ('Питон', 'Анаграмма', 'Простая')
# рандомное слово
word = random.choice(WORDS)
# пустая строка для букв
letter = ''
# закрытая строка с рандомным словом
letters = len(word) * '-'
# количество попыток
attempt = 5

print("\t\tДобро пожаловать в игру!")
print(f'\nУгадайте слово из {len(word)} букв , за {attempt} попыток.')
print('Теперь ты можешь 5 раз спросить меня, есть ли какая-то буква в этом слове?\n')

while attempt > 0:
    print(f'\nУ вас {attempt} попыток(и)')
    print('\t\t', letters)
    letter = input('Назовите букву: ')
    if letter in word:
        letters = letters[:word.find(letter)] + \
            letter + letters[word.find(letter)+1:]
        print('\nТакая буква есть в слове!')
    else:
        print("\nТакой буквы нет в этом слове. Попробуй еще.")
    attempt -= 1
    print('\t\t', letters)

answer = input('Какое слово было загадано? ')
answer = answer.capitalize()

if answer == word:
    print("\nПоздравляю!!! Вы угадали слово!!!")
else:
    print('Увы, Вы не угадали. Слово было:', word)

print('\tСпасибо за игру.')
input('\nНажмите Enter для выхода\n')
