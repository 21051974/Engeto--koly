import random
number=[]
attemps=0

print('=' * 92)
print("Hi there!, 'I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
print(' ')

def MakeNumer():
    for i in range(4):
        x=random.randint(0,9)
        number.append(x)

    if len(number)>len(set(number)):
        number.clear()
        MakeNumer()

def PlayGame():
    global attemps
    attemps=+1
    cows=0
    bulls=0
    print(number)
    choice=input("please enter a 4 digit number: ")
    guess=[]
    for i in range(4):
     guess.append(int(choice[i]))

    for i in range(4):
        for j in range(4):
            if (guess[i]==number[j]):
                cows+=1

    for x in range(4):
     if guess[x]==number[x]:
            bulls+=1

    print("Bulls:",bulls)
    print("Cows:",cows)

    if(bulls==4):
        print(" ")
        print("Correct, you've guessed the right number in 4 guesses!",attemps,"attemps!")
        print("That's {amazing, average, not so good, ...}")
    if(bulls!=4):
        PlayGame()

MakeNumer()
PlayGame()

print('=' * 65)