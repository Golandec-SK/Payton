
submenu = ("""
    Меню распределение очков'
    '0 - Вернуться'
    '1 - Распределить очки',
    '2 - Обнулить распределение'
""")
parameters = (
    'Сила',
    'Здоровье',
    'Мудрость',
    'Ловкость'
)
points = 30
choice = None
parameter = {}
while choice != 0:
    print("""
            Меню характеристик
    
    0 - Выход
    1 - Показать характеристики
    2 - Управление характеристиками
""")
    choice = int(input('\nВаш выбор: '))
    print()
    if choice == 0:
        print('До свидане.')
    elif choice == 1:
        while points > 0 and choice != 0:
            print("""
            Меню распределение очков
    0 - Вернуться
    1 - Распределить очки
    2 - Обнулить распределение
""")
            choice = int(input('Ваш выбор: '))
            print('\n')
            if choice == 0:
                print()
            elif choice == 2:
                skill = input('\nВведите навык: ')
                point = int(input('Сколько очков вы хотите потратить?: '))
                result = {skill: point}
                parameter.append(result)
                parameter.sort(reverse=True)
                parameter = parameter[:5]
                points -= point
            elif choice == 1:
                print('Навак\tОчки')
                for result in parameter:
                    skill, point = result
                    print(skill, '\t',)