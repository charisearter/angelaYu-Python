# Day 4 - Rock Papaer Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
player_choice = input("Choose 1, 2, or 3: ")

if player_choice == "1":
    print(rock)
elif player_choice == "2":
    print(paper)
elif player_choice == "3":
    print(scissors)
else:
    input("1= Rock; 2= Paper; 3= Scissors. Choose.")

computer_choice = random.choice([1,2,3])
if computer_choice == 1:
    print(rock)
elif computer_choice  == 2:
    print(paper)
elif computer_choice  == 3:
    print(scissors)


if player_choice == "1" and computer_choice == 2:
    print("You lose")
elif player_choice == "1" and computer_choice == 3:
    print("You win")
elif player_choice == "2" and computer_choice == 1:
    print("You win")
elif player_choice == "2" and computer_choice == 3:
    print("You lose")
elif player_choice == "3" and computer_choice == 2:
    print ("You win")
elif player_choice == "3" and computer_choice == 1:
    print ("You lose")
else:
    print("It's a tie")
