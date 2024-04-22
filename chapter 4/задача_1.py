start = int(input('\nВведите начальное значение: '))
finish = int(input('Введите конечное значение: '))
interval = int(input('Введите конечное значение: '))

for i in range(start, finish, interval):
    print(i,  end='')

input('\n\nНажмите Enter для выхода\n')
