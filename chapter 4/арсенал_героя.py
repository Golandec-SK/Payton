# арсенал героя
# демонстрирует создание кортежей
# создадим пустой кортеж

inventory = ()

# расмотрим его как условие
if not inventory:
    print('\nВы безоружны.')
input('\nНажмите enter, что бы продолжить.')
# теперь создадим кортеж
inventory = ('Меч',
             'кольчуга',
             'щит',
             'аптечка')

# выведем этот кортеж на экра
print('\nСодержимое инвентаря.')
print(inventory)

# вывести все элементы последовательно
print('\nИтак, в вашем арсенале:\n')
for item in inventory:
    print('\t', item)

input('\nНажмите Enter для выхода')
