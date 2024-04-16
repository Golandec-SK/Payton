import random

count = 0
eagle = 0
resko = 0

while count != 100:
    count += 1
    coin = random.randint(1,2)
    if coin == 1:
        eagle += 1
    else:
        resko += 1
print(f"Монету подбросили 100 раз из них орел {eagle} раз и решко {resko} раз")

input('\n\nНажмите Enter для выхода\n')