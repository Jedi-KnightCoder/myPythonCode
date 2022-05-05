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
game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? \n "))
# if choice < 3 and choice > 0:
#   print(game[choice])
# else: 
#   print("Try another number")

computer = random.randint(0, 2)
rck = 0 #0 for rock
papr = 1#1 for paper
scors = 2 #2 for scissors

if choice >= 3 or choice < 0:
  print("Invalid Number")
else: 
  
  your_choice = game[choice] 
  computer_choice = game[computer]
  print(your_choice)
  print(computer_choice)
# else:
#   print("Try Again")
#below I INDENTED all the if statements to fall under the first "IF" statement listed above so if THE VARIABLE "choice" was greater than 3 the code would stop
  if choice == rck and computer == scors:
    print(f"You win!")
  elif choice == scors and computer == papr:
    print(f"You Win! ")
  elif choice == papr and computer == rck:
    print(f"You Win!!")
  elif choice == computer:
    print(f"It's a Tie!!")
  else:
    print(f"You LOSE 😪")
  
  



