from asyncio import IncompleteReadError
from multiprocessing import RLock
import random


Comp_moves = ["R", "P", "S"]
computer = Comp_moves[random.randint (0,2)]
player = False

while player == False:
    player = input("Enter your move (R for Rock, P for Paper,S for Scissor): ")
    if computer == player:
        print("It's a tie!")
    elif player == 'R':
        if computer == 'P':
            print("You loose, Computer wins!")
        else:
            print("You win!")
    elif player == 'P':
        if computer == 'S':
            print("You loose, Computer wins!")
        else:
            print("You win!")
    elif player == 'S':
        if computer == 'R':
            print("You loose, Computer wins!")
        else:
            print("You win!")
    new_game = input("Do you want to play another round? (Yes/No) ")
    if new_game == 'Yes':
       player = False
    else:
       print("Thank you for playing!")
       break;

