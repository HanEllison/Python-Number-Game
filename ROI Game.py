import random   #import library to randomly generate card number and dice roll

#start game, get name and issue instructions to player
name = input(str("Please enter your name: "))
print("Hi, ", name, ". Welcome to the game!")
print("I have a pack of cards here numbered from 1 to 10.")
print("I've pulled out one card!")

#generate random numbers for card and dice roll
card = random.randint(1, 10)
diceRoll = random.randint(1, 6)


#add in options for if dice roll equals one turn vs. multiple turns ("guess"vs "guesses")
if diceRoll == 1:
    print("Can you guess what number it is? You have", diceRoll, "guess.")
else:
    print("Can you guess what number it is? You have", diceRoll, "guesses.")

#obtain guess from player
guess = int(input("Your guess: "))

#set dice roll to decrease with first guess to signify one turn taken
diceRoll = diceRoll - 1

#set score to zero so each turn/guess loop can increment by 1
score = 0

#while loop for every incorrect guess so long as the turns taken (dice roll)
#remains above zero
while diceRoll > 0 and guess != card:
    print("Incorrect! Try again.")
    print("You have this many guesses left:", diceRoll)
    score += 1
    newguess = int(input("New guess: ")) #intro new guess for loop

    if newguess != card:
        diceRoll -= 1
     #loop returns to top for as many rounds that guess != card and diceRoll remains above zero
    else:
        print("You guessed correctly. Well done!")
        score += 1
        with open("statistics.txt", "a+") as file: #function to open stats file and write name, score and "loss" or "win"
            file.write("\n")
            file.write(str(name) + " | " + "won" + " | " + str(score))
        file.close()

        file = open("statistics.txt", "r") #to print stats to screen for player
        print(file.read())
        file.close()
        break

#function for if card is guessed correctly on first try
else:
    if guess == card:
        print("You guessed correct! Winner, winner, chicken dinner!")
        score += 1

        with open("statistics.txt", "a+") as file:
            file.write("\n")
            file.write(str(name) + " | " + "win" + " | " + str(score))
        file.close()

        file = open("statistics.txt", "r")
        print(file.read())
        file.close()
    else: 
        print("Wrong! Game over, friend.")
        with open("statistics.txt", "a+") as file:
            file.write("\n")
            file.write(str(name) + " | " + "loss" + " | " + str(score))
        file.close()

        file = open("statistics.txt", "r")
        print(file.read())
        file.close()

#function for if dice roll/number of gueeses left reaches zero




