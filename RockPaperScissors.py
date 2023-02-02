import random

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

#Write your code below this line 👇
user_choice = input("Choose rock, paper, or scissors: ")
if user_choice == "rock":
  print("You chose rock!", rock)
if user_choice == "paper":
  print("You chose paper!", paper)
if user_choice == "scissors":
  print("You chose scissors!", scissors)

computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print("Your opponent chose rock!", rock)
elif computer_choice == 1:
  print("Your opponent chose paper!", paper)
else:
  print("Your opponent chose scissors!", scissors)

if user_choice == "rock" and computer_choice == 0:
  print("It's a tie!")
elif user_choice == "rock" and computer_choice == 1:
  print("You lose!")
elif user_choice == "rock" and computer_choice == 2:
  print("You win!")
elif user_choice == "paper" and computer_choice == 0:
  print("You win!")
elif user_choice == "paper" and computer_choice == 1:
  print("It's a tie!")
elif user_choice == "paper" and computer_choice == 2:
  print("You lose!")
elif user_choice == "scissors" and computer_choice == 0:
  print("You lose!")
elif user_choice == "scissors" and computer_choice == 1:
  print("You win!")
else:
  print("It's a tie!")

