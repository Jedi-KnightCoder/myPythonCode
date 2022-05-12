from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

print("Welcome to the Auction Program.")

bid = {}
bidding_finished = False #this supposes that bidding isn't complete

def highest_bidder(bid_record):
  highest_bid = 0
  #{key: "value","John": "$345", "Sarah": "$56"}
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"THe winner is {winner}, at {highest_bid}")

#My Code
while bidding_finished == False:
  name = input("What is your name? ")
  price = int(input(f"What's your bid? $ ")) 
  bidders = input("Are there any other users that want to bid? Please Type yes or no? ").lower()
  bid[name] = price
  if bidders == "yes":
      clear()            
      print(bid)
    
  else:
    bidding_finished = True
    #print(bid)
    highest_bidder(bid_record=bid)
  
#def auction(bid_name, bid_price, other_bidders):  
  #bid_list = []
    #bid[bid_name] = bid_price
    
    
      
      # highest_bidder()
      # max = max(bid)
      # print(max)
      #clear()   
  
# auction(bid_name=name, bid_price=price, other_bidders=bidders)

# def highest_bidder():
      
#     for key in bid: 
#       print(key)
# highest_bidder()


      #   max = max(key)    
      #   print(max)
      #   print(key)
        
        # print(max(key))
        #print(bid)
        # bid_list.append(bid[key])
        # print(bid_list)
  #print(max(bid[key]))

                
     
                
      
      
    
    
  
#bid = {name:price}  



# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
  # if bidders == "yes":
  #   print(bid)
  #   clear()
  #   #auction(bid_name = name, bid_price = price)   
  # else:
  #   reset == False
    
  #   print("You have Ended the Program. ")        
  #   print(bid)