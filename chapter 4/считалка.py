# считалка
# использует функции range()

print('Подсчитаем: ')

for i in range(10):
    print(i, end=' ')

print('\n\nПеречислим кратное 5')
for i in range(0, 50, 5):
    print(i, end=' ')

print('\n\nПосчитаем в обратном порядке')
for i in range(10, 0, -1):
    print(i, end=' ')

input('\n\nНажмите Enter для выхода\n')
