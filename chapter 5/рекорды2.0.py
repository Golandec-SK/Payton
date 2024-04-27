# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None
while choice != 0:
    print(
        """
    Рекорды 2.0
0 - Выйти
1 - Показать рекорды
2 - Добавить рекорды
3
"""
    )
    choice = int(input('Ваш выбор: '))
    print()
# выход
    if choice == 0:
        print('До свидане.')
# вывод таблицы рекордов
    elif choice == 1:
        print('Рекорды\n')
        print('ИМЯ\tРЕЗУЛЬТАТ')
        for entry in scores:
            score, name = entry
            print(name, '\t', score)
# добовление результата как вложенного кортежа add a score
    elif choice == 2:
        name = input('Впишите имя игрока: ')
        score = int(input('Впишите результат: '))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
# непонятный пользовательский ввод
    else:
        print('Извините, в меню нет пнкта', choice)
input('\nНажмите Enter, чтобы выйти\n')
