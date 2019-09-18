def check_birthdate(num1,num2,num3)
if num1 > 31 or num2 > 12 or num3 > 2019:
return False
else:
	return True

from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - 
         ((today.month, today.day) < 
         (birthDate.month, birthDate.day)) 
  
    return age 
print(calculateAge(date(1997, 2, 3)), "years")
# last part needs clarification
