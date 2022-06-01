from art import logo, vs
from game_data import data
import random

do_continue = True
score = 0
new = ""
new_follower_count = ""
change = False
while do_continue :
  player_a = random.choice(data)  
  player_b = random.choice(data)
  follower_count_a = player_a['follower_count']
  follower_count_b = player_b['follower_count']

  if change and score > 0:
    player_a = new
    follower_count_a = new_follower_count
    
  # if change:
  #   player_a = new
  
  print(logo)
  
  print(f"Compare A: {player_a['name']} , {player_a['description']} from {player_a['country']}", follower_count_a)
  
  print(vs)
  print(f"Against B: {player_b['name']} , {player_b['description']} from {player_b['country']}", follower_count_b)
  if score > 0:
    print(f"Score is {score}")
  
  choice = input("Who has more followers 'A' or 'B'? ").lower()
  # print("test")
  # do_continue = False
  if follower_count_a > follower_count_b and choice == "a":
    # print("test")
    # if choice == "a":
    score += 1
    print(f"Score is {score}")
    new = player_b    
  elif follower_count_b > follower_count_a and choice == "b":
    # print("test")
    # if choice == "b":
    change = True
    new = player_b    
    new_follower_count = follower_count_b       
    score += 1
    print(f"Score is {score}")    
    
  else:
    do_continue = False
    print(f"Final Score is {score}")    
    
    



# print(compare_a)
# print(player_a)
# print(player_a["name"])



