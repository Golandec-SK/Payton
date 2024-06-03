# Запишим
# Демонстрирует запись в фаил

print('Создаю текстовый фаил методом write().')
text_file = open('write_it.txt', 'w', encoding='utf-8')
text_file.write('Строка 1\n')
text_file.write('Это строка 2\n')
text_file.write('Этй строке достался строка 3\n')
text_file.close()

print('\nЧитаю вновь созданные файлы')
text_file = open('write_it.txt', 'r', encoding='utf-8')
print(text_file.read())
text_file.close()

print('\nСоздаю текстовый файл методом writelines().')
text_file = open('write_it.txt', 'w', encoding='utf-8')
lines = ['Строка 11\n',
         'Это строка 2\n',
         'Этй строке достался строка 3\n']
text_file.writelines(lines)
text_file.close()

print('\nЧитаю вновь созданные файлы')
text_file = open('write_it.txt', 'r', encoding='utf-8')
print(text_file.read())
text_file.close()

input('\n\nНажмите Enter? что бы выйти')