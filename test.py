import random 

def main(number): 
    number = int(input("Введите загаданное число: ")) 
    low = 1 
    high = 100 
    tries = 1 

    while True: 
        computer_number = random.randint(low, high) 
        print('Загаданное число равно, больше или меньше', computer_number) 
        ansver = int(input('1 - равно, 2 - больше, 3 - меньше:')) 

        if ansver == 1: 
            print('Компьютер угадал число', tries, "попыток") 
            break 
        elif ansver == 3: 
            high = computer_number - 1 
        elif ansver == 2: 
            low = computer_number + 1 
        tries += 1 
    if __name__ == "__main__":
main()