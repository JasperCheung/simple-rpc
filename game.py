import random
#replaces the input lines if its python3
def start():

    player_choice = -1
    comp_choice = -1
    choices = ["Rock", "Paper", "Scissors"]
    winners = [1,2,0]

    while(player_choice > 2 or player_choice < 0):

        print("enter a choice:")
        print("0 for Rock")
        print("1 for Paper")
        print("2 for Scissors")
        try:
            #player_choice = int( input())
            player_choice =  input()

        except:
            print ("Not a number")


    print("Your Choice: "+choices[player_choice])
    #computer choice
    #a <= N <= b
    comp_choice = random.randint(0,2)
    print(comp_choice)
    print("Computers Choice: " + choices[comp_choice])

    if comp_choice is player_choice:
        print ("Tie, Both players choose the same number")

    elif winners[player_choice] == comp_choice:
        print("Computer wins, %s beats %s" % (choices[comp_choice], choices[player_choice] ))

    else:
        print("Player wins, %s beats %s" % (choices[player_choice], choices[comp_choice] ))

    #again = input("do you want to play again?[Y/N]:")
    again = raw_input("do you want to play again?[Y/N]:")

    if again == "Y":
        start()
    else:
        return 0







start()
