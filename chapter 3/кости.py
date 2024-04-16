# Кости
# Демонстрирует генерацию случайных чисел
import random
# создаем диапазон случайных чисел от 1 - 6

first = random.randint(1, 6)
second = random.randrange(6) + 1
total = first + second

print(f'При вашем броске выпало {first} и {second} очков в сумме {total}')
print('\n\n Нажмите Enter для выхода')