# Привередливая считалка
# Демонстрирует работу break и continue
count = 0
while True:
    count += 1

    # завершение цикла если count принимает значение 10
    if count > 10:
        break

    # пропустить 5
    if count == 5:
        continue
    print(count)

input('\n\nНажмите Enter для выхода\n') 
