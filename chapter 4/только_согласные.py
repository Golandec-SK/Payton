# только согласные
# демонстрирует, как создовать новые строки из исходных с помощью цикла for

message = input('Введите текст: ')
new_message = ''
VOWELS = 'овшкьсжцзoeolsgd'
print()

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print('Создана новая строка:', new_message)
print('\nВот ваш текст с изьятыми гласными буквами:', new_message)

input('\n\nНажмите Enter для выхода\n')