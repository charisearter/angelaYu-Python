#day 3 Project Treasure Island Project
'''
Treasure Island text based game
The gamer in me came out and I had to make it work properly by adding a while loop checking if the player was still alive and for the game to end when they died.

Might come back later and expand more on it.
'''

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
player_alive = True
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

while player_alive: # reads as true
    print("You come to a split in the path.")
    path_chosen = input("Do you want to go left or right?")

    if path_chosen == "left":
        print("You chose to go left")
    else:
        print("You chose to go right.\n")
        print("You fell into a hole. GAME OVER")
        player_alive = False
        break

    print("You arrive at a large lake.\n")
    chosen_action = input("Do you want to swim or wait?")

    if chosen_action == "wait":
        print("You chose to wait.\n")
    elif chosen_action == "swim":
        print("You chose to swim.\n")
        print("You were attacked by trout. GAME OVER")
        player_alive = False
        break

    print("3 doors appeared.\n")
    door_picked = input("Pick a door. Blue, Yellow, or Red.")

    if door_picked == "Blue":
        print("You picked the Blue door\n")
        print("You were eaten by beasts. GAME OVER")
        player_alive = False
        break
    elif door_picked == "Yellow":
        print("You picked the Yellow door\n")
        print("You found the treasure! You Win!")
    elif door_picked == "Red":
        print("You picked the Red door\n")
        print("You were burned by fire. GAME OVER")
        player_alive = False
        break
    else:
        print("You picked nothing and was never seen again. GAME OVER")
        player_alive = False
        break
