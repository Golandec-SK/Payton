# Рекорды
# Демонстрирует списочные методы
scores = []
choice = None
while choice != 0:
    print(
        """
Рекорды
0 - Выйти
1 - Показать рекорды
2 - Добавить рекорды
3 - Удалить рекорды
4 - Сортировать список
"""
    )
choice = int(input('Ваш выбор: '))
print()
# выход
if choice == 0:
    print('До свидане.')
# вывод лучших результатов на экран циклом for
elif choice == 1:
    print('Рекорды\n')
    for score in scores:
        print(score)
# добавляем рекорда методом append()
elif choice == 2:
    score = int(input('Впишите свой результат: '))
    scores.append(score)
# удаление рекорда методом remove()
elif choice == 3:
    score = int(input('Какой из рекордов удалить?: '))
    if score in scores:
        scores.remove(score)
    else:
        print(f'Результат {score} не содержится в списке рекордов.')
# сортировка рекордов методом sort()
elif choice == 4:
    scores.sort(reverse=True)
# непонятный пользовательский ввод
else:
    print('Извините, в меню нет пнкта', choice)
input('\nНажмите Enter, чтобы выйти\n')
