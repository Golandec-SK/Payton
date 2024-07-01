# обработаем
# демонстрирует обработку исключительных ситуаций 
# try/except
try:
    num = float(input('Введите чмсло: '))
except:
    print('Похлже это не число')


# обработка исключенияч определенного типа
try:
    num = float(input('Введите чмсло: '))
except ValueError:
    print('Это не число!')


# обработка исключений нескольких разных типов
print()
for value in (None, 'Привет!'):
    try:
        print('Пытаюсь прелброзовать в число: ', value, '-->', end=' ')
        print(float(value))
    except (TypeError, ValueError):
        print('Похоже, это не число!')

print()
for value in (None, 'Привет!'):
    try:
        print('Пытаюсь прелброзовать в число: ', value, '-->', end=' ')
        print(float(value))
    except TypeError:
        print('Я умею преоброзовывать только строки в число!')
    except ValueError:
        print('Я умею преоброзовывать только строки, составленные из цифр')


# получение аргумента
try:
    num = float(input('Введите чмсло: '))
except ValueError as e:
    print('Это не число! Итерпретатор как бы нам говорит:')
    print(e)
    