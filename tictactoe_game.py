from os import system, name 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
#This where the users' inputs for printing will be stored
inputs = ["","","","","","","","",""]
won = ""
#this is will help us check who has won a game at any given point
class Player:
    def __init__(self,name):
        self.name = name
        self.plays = ["","","","","","","","",""]


#This will help us print the status of our board after each user move
def print_board(li):
    i = 0
    while i<9:
        if li[i] == "":
            if li[i+1] == "":
                if li[i+2] == "":
                    print("| "+str(i+1)+" | "+str(i+2)+" | "+str(i+3)+" |")
                else:
                    print("| "+str(i+1)+" | "+str(i+2)+" | "+li[i+2]+" |" )
            else:
                if li[i+2] == "":
                    print("| "+str(i+1)+" | "+li[i+1]+ " | "+str(i+3)+" |")
                else:
                    print("| "+str(i+1)+" | "+li[i+1]+" | "+li[i+2]+" |" )
        else:
            if li[i+1] == "":
                if li[i+2] == "":
                    print("| "+li[i]+" | "+str(i+2)+" | "+str(i+3)+" |")
                else:
                    print("| "+li[i]+" | "+str(i+2)+" | "+li[i+2]+" |" )
            else:
                if li[i+2] == "":
                    print("| "+li[i]+" | "+li[i+1]+ " | "+str(i+3)+" |")
                else:
                    print("| "+li[i]+" | "+li[i+1]+" | "+li[i+2]+" |" )
        

        #printing a lne to indicate new row
        if i != 6:
            print("-------------")
        #increment by 3 cuz why not
        i+=3

#we want to check if a nigga is winning 
def check_for_win(user):
    #This func returns a size 2 tuple.
    #A 0 at index 0 of the tuple indicates that the user hasn't inputted enough values to declare them as a winner, so there is no need to clear their plays
    #A 1 at index 0 of the tuple indicates that the user has inputted enough values to declare them as a winner, so now we check if he or she has won
    #A 0 at index 1 of the tuple indicates that the user is off the right track of winning and their plays should be cleared up
    #A 1 at index 1 of the tuple indicates that the user is on the right track of winning and they should play smart
    if user.plays[0] != "":
        if user.plays[1] != "":
            if user.plays[2] != "":
                return 1
    if user.plays[0] != "":
        if user.plays[3] != "":
            if user.plays[6] != "":
                return 1
    if user.plays[0] != "":
        if user.plays[4] != "":
            if user.plays[8] != "":
                return 1
    if user.plays[2] != "":
        if user.plays[5] != "":
            if user.plays[8] != "":
                return 1
    if user.plays[2] != "":
        if user.plays[4] != "":
            if user.plays[6] != "":
                return 1
    if user.plays[3] != "":
        if user.plays[4] != "":
            if user.plays[5] != "":
                return 1
    if user.plays[1] != "":
        if user.plays[4] != "":
            if user.plays[7] != "":
                return 1
    if user.plays[6] != "":
        if user.plays[7] != "":
            if user.plays[8] != "":
                return 1
    else: 
        return 0

#We would also like to check if the game ends as a tie
def check_for_tie(li):
    filled = 1
    for i in li:
        if i == "":
            filled = 0
    return filled

#Now that we can print our board and know our winner or draw, it's time to code the actual game

#Know the players
clear()
print("Who is player1?")
name1 = input("Name: ")
clear()
player1 = Player(name1)
let1 = ""
while 1:
    print("Which icon do you want to use?")
    let1 = input("x or o: ")
    if let1 == 'x':
        break
    elif let1 == 'o':
        break
    else:
        clear()
        print("invalid icon, try again")
clear()
print("Who is player2?")
name2 = input("Name: ")
clear()
player2 = Player(name2)
if let1 == "x":
    let2 = "o"
else:
    let2 = "x"

#Now for the game

while 1:
    played_1 = 1
    x = ""
    while played_1:
        print("Player 1's turn.")
        print("What position do you want to fill")
        print_board(inputs)
        x = input("Number: ")
        #checking if the position is already filled up
        if inputs[int(x)-1] != "":
            clear()
            print("This position is already filled")
        else:
            played_1 = 0
    clear()
    inputs[int(x)-1] = let1
    player1.plays[int(x)-1] = let1
    winner = check_for_win(player1)
    # if winner[0] == 0:
    #     if winner[1] == 0:
    #         player1.plays = []
    #         player1.plays.append(int(x))
    # else:
    #     if winner[1] == 0:
    #         player1.plays = []
    #         player1.plays.append(int(x))
    if winner == 1:
        won = "player1"
        break
    
    #check for a draw
    if check_for_tie(inputs):
        won = "tie"
        break
    played_1 = 1
    while played_1:
        print("Player 2's turn.")
        print("What position do you want to fill")
        print_board(inputs)
        x = input("Number: ")
        #checking if the position is already filled up
        if inputs[int(x)-1] != "":
            clear()
            print("This position is already filled")
        else:
            played_1 = 0
    clear()
    inputs[int(x)-1] = let2
    player2.plays[int(x)-1] = let2
    winner = check_for_win(player2)
    if winner == 1:
        won = "player1"
        break

    #no need to check for draw as a draw only happens after the first player's move
    
    
print_board(inputs)
if won == "tie":
    print("The game ended as a tie")
elif won == "player1":
    print(player1.name + " won!!!")
else:
    print(player1.name + " won!!!")