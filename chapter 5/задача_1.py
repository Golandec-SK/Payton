import random
roster = ['Конь', 'Жук', 'Собака', 'Эльф']

for i in range(len(roster)):
    rosters = random.choice(roster)
    print(rosters)
    roster.remove(rosters) 