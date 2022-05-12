def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "True" #print("Leap year.")
      else:
        return "False" #print("Not leap year.")
    else:
      return "True" #print("Leap year.")
  else:
    return "False" #print("Not leap year.")
  
def days_in_month(year, month):   
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  dictionary = ["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  month -= 1
  #is_leap(year)
  if is_leap(year) == "True":
    month_days[1] = 29
    how_many_days = month_days[month]  
    
  else:     
    how_many_days = month_days[month] 
    #print(is_leap(year))
  return how_many_days
    #return f"There are {how_many_days} days in the month of {dictionary[month]}"    
#is_leap(year)
#new_year = is_leap(year)
# return is_leap(year)
# days_in_month()
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












