
parameters = {
    'Сила': 0,
    'Здоровье': 0,
    'Мудрость': 0,
    'Ловкость': 0
}
points = 30
choice = None

while choice != 0:
    print("""
            Меню характеристик

    0 - Выход
    1 - Показать характеристики
    2 - Распределить очки навык
    3 - Обнулить распределение
""")
    choice = int(input('\nВаш выбор: '))
    print()
    if choice == 0:
        print('До свидане.')
    elif choice == 1:
        for key, value in parameters.items():
            print(f'{key} -- {value}')
        input('\nНажмите Enter, чтобы продолжить\n')
    elif choice == 2:
        print('\n\tХарактеристики.\n')
        for i in parameters:
            print(i)
        skill = input('\nВведите навык: ')
        skill = skill.capitalize()
        if skill in parameters:
            point = int(input('Сколько очков вы хотите потратить?: '))
            parameters[skill] = point
            print(f'Вы добавили {point} очков в навак: {skill}')
            points -= point
            print(f'\nУ вас осталось {points} очка(ов)')
        else:
            print('Некорректный ввод! Попробуйте еще раз.')
        input('\nНажмите Enter, чтобы продолжить\n')
    elif choice == 3:
        parameters[skill] = 0
        print('Ваши навыки сброшены.')
        input('\nНажмите Enter, чтобы продолжить\n')
    else:
        print('Извините, в меню нет пнкта', choice)

input('\nНажмите Enter, чтобы выйти\n')
