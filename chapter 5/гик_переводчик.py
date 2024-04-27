# Перевод с гигмкого на русский
# Демонстрирует использования словарей
geek = {'404': 'Не знать, не владеть информацией. 404 "Страница не найдена".',
        'Googling': 'Поиск сведений о ком-либо.',
        'Keyboard Plaque': 'Мусор, который скапливаеться в клавиатуре.',
        'Link Rot': 'Процес установления гиперссылок на веб-стоанице',
        'Percussive Maintence': 'Ситуация, когда бьют неисправный технику',
        'Uninstalled': 'Об увольнении кого-либо'
        }
scores = []
choice = None
while choice != 0:
    print(
        """
    Переводчик с гикского на русский\n
0 - Выйти
1 - Найти толкование термина
2 - Добавить термин
3 - Изменить толкование
4 - Удалить термин
"""
    )
    choice = int(input('Ваш выбор: '))
    print()
# выход
    if choice == 0:
        print('До свидане.')
# вывод лучших результатов на экран циклом for
    elif choice == 1:
        for key in geek.keys():
            print(key)
        term = input('\nКакой термин вы хотите перевести?: ')
        if term in geek:
            definition = geek[term]
            print(f'\n{term} - означает {definition}')
        else:
            print('\nУвы, этот термин мне незнаком', term)
# добовление термина с толкованием
    elif choice == 2:
        for key in geek.keys():
            print(key)
        term = input('\nКакой термин вы хотите изменить?: ')
        if term not in geek:
            definition = input('Впишите ваше толкование: ')
            geek[term] = definition
            print(f'\nТерминv - {term}, добавлен в словарь')
        else:
            print('\nТакой термин уже есть!')
# Новое толкование известного термина
    elif choice == 3:
        for key in geek.keys():
            print(key)
        term = input('\nКакой термин вы хотите переопределить?: ')
        if term in geek:
            definition = input('Ваше толкование: ')
            geek[term] = definition
            print(f'\nТермин - {term}, переопределен.')
        else:
            print('\nТакого термина пока нет! Попробуй добавить его в словарь')
# удаление термина с его толкованием
    elif choice == 4:
        for key in geek.keys():
            print(key)
        term = input('\nКакой термин вы хотите удалить?: ')
        if term in geek:
            del geek[term]
            print(f'Термин - {term}, удален.')
        else:
            print('\nТакого ьермина нет! Попробуйте добавить его в словарь')
    else:
        print('Извините, в меню нет пнкта', choice)
input('\nНажмите Enter, чтобы выйти\n')
