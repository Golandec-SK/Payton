# резчик пици
# демонстрирует мрезы строк

word = 'пицца'
memo = """
  Slicing 'Cheat Sheet'

  0   1   2   3   4   5
  +---+---+---+---+---+
  | п | и | ц | ц | а |
  +---+---+---+---+---+
 -5  -4  -3  -2  -1

"""

start = None
while start != "":
    print(memo)
    print('Введите начальный и конечный индекс для среза "пица".')
    print('Для выхода нажмите enter, не вводя начальную позицию')

    start = (input('\nНачальная позиция: '))

    if start:
        start = int(start)
        finish = int(input('Конечная позиция: '))
        print('Срез word[', start, ':', finish, '] выглядит как', end=" ")
        print(word[start:finish])

input('\n\nНажмите Enter для выхода\n')
