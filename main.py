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
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print("You chose rock")
  print(rock)
if choice == 1:
  print("You chose paper")
  print(paper)
if choice == 2:
  print("You chose scissors")
  print(scissors)


computer_choice = random.randint(0,2)
if computer_choice == 0:
  print("Computer chose rock")
  print(rock)
if computer_choice == 1:
  print("Computer chose paper")
  print(paper)
if computer_choice == 2:
  print("Computer chose scissors")
  print(scissors)

if computer_choice == 2 and choice == 1:#scissors vs paper
  print("Computer wins!")
elif computer_choice == 1 and choice == 0:
  print("Computer wins!")
elif computer_choice == 0 and choice == 2:
  print("Computer wins!")
elif computer_choice == 2 and choice == 0:
  print("You win!")
elif computer_choice == 1 and choice == 2:
  print("You win!")
elif computer_choice == 0 and choice == 1:
  print("You win!")
else:
    print("Tie!")



