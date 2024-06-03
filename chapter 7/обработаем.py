# Обработаем
# Демонстрирует обработку исключений ситуаций
# try/except
try:
    num = float(input('Введите число:'))
except:
    print('Похлже это не число!')

# обработка исключений определенрго типа
try:
    num = float(input('Введите число:'))
except ValueError:
    print
