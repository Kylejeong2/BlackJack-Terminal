import random
import sys

#set of cards
deck = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king", "ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king", "ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king", "ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king"]

#the game itself
def game_start():
    #calculate computer score
    computer_score = random.randint(15, 21)

    #run through game with player
    a = random.choices(deck, k=2)

    #get value from list
    cards = [a[0], a[1]]
    print("Your cards are: " + str(a[0]) + " and " + str(a[1]) + "\n")

    #initialize hit and stand
    hit_stand = ""

    while hit_stand != 's':
        hit_stand = input("Would you like to Hit or Stand? \n 'h' to hit & 's' to stand:  ")
        if hit_stand == 'h':
            new_card = random.choices(deck, k=1)
            cards.append(new_card[0])
        #log cards
        print("Your cards are: ")
        for i in range(len(cards)):
            print(cards[i])

    #create new list for value of cards
    value_cards = []

    for i in range(len(cards)):
        if type(cards[i]) == str:
            if str(cards[i]) == "ace":
                choose = input("If you want your ace to be 1, press 'y' and then the enter key\nIf you want your ace to be 11, press any other key and then enter:  ")
                if choose == 'y':
                    cards[i] = 1
                cards[i] = 11
            if cards[i] == "king" or cards[i] == "queen" or cards[i] == "jack":
                cards[i] = 10
        value_cards.append(cards[i])

    total = sum(value_cards)
    print("Your total score was " + str(total))
    print("The computer's score was " + str(computer_score))

    #see who won the game
    if total == 21 and computer_score == 21:
        print("The game was a Tie!")
    if abs(total - 21) <  abs(computer_score - 21):
        print("YOU WIN!!!!")
    if abs(total - 21) >  abs(computer_score - 21) or total > 21:
        print("You lose!!!!")
    
#intro
start = input("Welcome to Blackjack \n To start the game, enter the letter 's'. ")
#game start 
if start == 's':
    game_start()
else:
    sys.exit(0)