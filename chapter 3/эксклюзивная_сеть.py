# Эксклюзивная сеть
# Демонстрирует состовные условия и логичесеские операторы

security = 0
userName = ''
password = ''

while not userName and not password:
    userName = input('Введите логин: ')
    password = input('Введите пароль: ')

if userName == 'M.Dawson' and password == 'secret':
    print('Привет, Майк')
    security = 5

elif userName == 'S.Miymoto' and password == 'mariobros':
    print('Доброго времени суток, Сигеру.')
    security = 3

elif userName == 'guest' or password == 'guest':
    print('Добро пожаловать к нам в гости')
    security = 1

else:
    print('Войти в систему не удалось. Должно быть. вы не очень то эксклюзивный гражданин.\n')

input('\n\nНажмите Enter для выхода\n')
