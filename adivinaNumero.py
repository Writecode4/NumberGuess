import random


print('==================')
print('Start the game')
top = int(input('Highest number: '))
bottom = int(input('Lowest number: '))
x = int(input('My number is: '))

def give_number(x):
    global top
    global bottom
    rec = []
    attempts = 5
    while attempts > 0:
        guess = random.randint(bottom, top)
        
        if guess == x:
            print(guess)
            print('You win!, good comp')
            attempts = 0
        elif guess in rec:
            print(guess)
            print(f'{guess}?? You said that!, you lost 1 attempt')
            attempts -= 1
        elif guess > x and guess not in rec:
            print(guess)
            print("It's lower, try again")
            attempts -= 1
            top = guess
            rec.append(guess)
        elif guess < x and guess not in rec:
            print(guess)
            print("It's higher, try again")
            attempts -= 1
            bottom = guess
            rec.append(guess)
        

    print('The game is over')

give_number(x)       
