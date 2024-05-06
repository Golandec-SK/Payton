# День рождения
# Демонстриркет именованные аргументы и значения параметров по умолчанию.
# позиционные параметры
def birthday1(name, age):
    print(f'С днем рождения, {name}! Вам сегодня исполняеться {age},\
не так ли?\n')
# параметры со значениями по умолчанию


def birthday2(name='товарищь Иванов', age=1):
    print(f'С днем рождения, {name}! Вам сегодня исполняеться {age},\
не так ли?\n')


birthday1('товарищь Иванов', 1)
birthday1(1, 'товарищь Иванов')
birthday1(name='товарищь Иванов', age=1)
birthday1(age=1, name='товарищь Иванов')
birthday2()
birthday2(name='Катя')
birthday2(age=12)
birthday2(name='Катя', age=12)
birthday2('Катя', 12)

input('\n\nНажмите Enter, что выйти.')
