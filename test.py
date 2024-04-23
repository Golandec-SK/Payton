input('Если готов играть, нажми Entr')
slova=('сосиска',
       'крокодил',
       'медведь',
       'завтрак',
       'компьютер')
import random
slovo=random.choice(slova)
print('В этом слове', len(slovo),'букв')
print('Теперь ты можешь 5 раз спросить меня, есть ли какая-то буква в этом слове?\n')
for _ in range (5):
    bukva=input('Напиши букву, которую хочешь проверить?')
    if bukva in slovo:
        print('Да')
    else:
        print('Нет')
otgadka=input('Какое слово было загадано?\n')
if otgadka==slovo:
    print('Ура, ты угадал!')
else:
    print('Нет, попробуй в другой раз')
input='Для выхода нажмите Entr'