############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random
from art import logo
from replit import clear

print(logo)
#input("Do you want to play a game of BlackJack?  Type 'y' or 'n ' ").lower()

def deal_card():
    """Returns a Random Card from the Deck"""
    #input("Do you want to play a game of BlackJack?  Type 'y' or 'n ' ").lower()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0 #+ "BlackJack!!!!!"

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "It's a Draw"
    elif computer_score == 0:
        return "You Lose, the Computer has a BlackJack"
    elif user_score == 0:
        return "You Win!, You have a Blackjack"
    elif user_score > 21:
        return f"You Lose, you went over 21 computer score is {computer_score}, your score {user_score}"
    elif computer_score > 21:
        return f"You Win, the computer went over 21 computer score is {computer_score}, your score {user_score}"
    elif user_score > computer_score:
        return f"You win, you have a higher score, computer score is {computer_score}, your score {user_score}"

    else:
        return f"you lose, the computer has a higher score computer score is {computer_score}, your score {user_score}"


def play_game():
  from art import logo
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
  while not is_game_over:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards[0]}")
      if user_score == 0 or computer_score == 0 or user_score > 21:
          is_game_over = True
          print("ok")
      else:
          deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
          if deal_again == "y":
              user_cards.append(deal_card())
              print(sum(user_cards))
  
          else:
              is_game_over = True
              print("Game is Finished")
  while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
      print(f"Computer's score is {computer_score}")
  
  print(compare(user_score, computer_score))

while input("Would you like to play a game of BlackJack? Type 'y' or 'n' ") == "y":
  clear()
  play_game()
  #     print("hello")