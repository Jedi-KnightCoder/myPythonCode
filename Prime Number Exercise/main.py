#Write your code below this line 👇





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
 
n = int(input("Check this number: "))
def prime_checker(number):   
  is_prime = True 
  for i in range(2, number):
     if number % i == 0:
      is_prime = False 
  if is_prime:
    print("It's a Prime number")
  else:
    print("It's not a prime number")
prime_checker(number=n)  
  
  # if n % 2 == 0:
  #   print(f"{n} is not a prime number")
  # elif n % 3 == 0:
  #   print(f"{n} is not a prime number")
  # elif n % 5 == 0:
  #   print(f"{n} is not a prime number")
  # else:
  #   print(f"{n} is a prime number")
 
    
  





