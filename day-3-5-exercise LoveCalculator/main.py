# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
you = name1.lower()
yourLover = name2.lower()

t = you.count("t") + yourLover.count("t")
r = you.count("r") + yourLover.count("r")
u = you.count("u") + yourLover.count("u")
e = you.count("e") + yourLover.count("e")

l = you.count("l") + yourLover.count("l")
o = you.count("o") + yourLover.count("o")
v = you.count("v") + yourLover.count("v")
e = you.count("e") + yourLover.count("e")

love_score = str(t + r + u + e) + str(l + o + v + e) 
newscore = int(love_score)

if (newscore < 10) or (newscore > 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (newscore >=40) and (newscore <=50):
  print(f"Your love score is {love_score}, you are alright together.")
else: print(f"Your love score is {love_score}")
            
# print(love_score,"%")


#print(type(name1))


