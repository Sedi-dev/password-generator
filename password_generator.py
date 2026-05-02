#password generator
#Lesedi Mohale
#24 April 2026

import random
import string

def generator(length, strength):
   """ 
   Generates secure passwords based on user-selected strength: 
   weak, medium, strong.
   """
   
   lower = string.ascii_lowercase 
   upper = string.ascii_uppercase
   digit = string.digits
   symbol = '!@#$%_-/'

   # Define character pools based on strength
   if strength == "Weak":
      chars = lower
      
   elif strength == "Medium":
      chars = lower + upper + digit
      
   else:
      chars = lower + upper + digit + symbol     
   
   password = []
   
   # Gaurantees complexity
   if strength in ["Medium", "Strong"]:
      password.append(random.choice(lower))
      password.append(random.choice(upper))
      
   if strength == "Strong":
      password.append(random.choice(digit))
      password.append(random.choice(symbol))
      
   # Fill remaining characters randomly
   while len(password) < length:
      password.append(random.choice(chars))
   
   random.shuffle(password)
   
   #convert to string
   pass_word = "".join(password)
          
   return pass_word
   
def get_strength():
   """ Let user choose password strength. """
   
   while True:
      print("\n--- Choose strength:")
      print("1 - Weak(not recommended)")
      print("2 - Medium")
      print("3 - Strong(recommended)")
      
      choice = input("Enter choice (1/2/3):\n")
      
      if choice == "1":
         return "Weak"
      elif choice == "2":
         return "Medium"
      elif choice == "3":
         return "Strong" 
      else: 
         print("Invalid choice")
         
def strength_score(password, strength):
   """
   Returns a strength score (0-100) based on password:
   length + character variety + strength level.
   """
   score = 0
   
   # Length scoring
   if len(password) >= 10:
      score += 40
   elif len(password) >= 8:
      score += 30
   elif len(password) >= 6:
      score += 20   
   else:
      score += 10
   
   # Character variety checks
   if any(p.islower() for p in password):
      score += 15
   elif any(p.isupper() for p in password):
      score += 15  
   elif any(p.isdigit() for p in password):
      score += 15
   elif any(p in "!@#$%_-/" for p in password):
      score += 15   
         
   # Strength bonus (based on user choice) 
   if strength == "Strong":
      score += 10
   elif strength == "Medium":
      score += 5
      
   return min(score, 100)

def main():
   
   print("🔐 Password Generator Tool")
  # Keep asking for length until valid input is given
  
   while True: 
      try:
         length = int(input("Enter password length:\n"))
         
         if length < 4:
            
            print("Password must be at least 4 characters")
            continue
         
         break
      
      except ValueError:
         print("Please enter a valid number")   
         
   strength = get_strength()
   
   password = generator(length, strength)
   
   score = strength_score(password, strength)
   
   # Interpret score
   if score >= 80:
      level = "Strong 🔴"
   elif score >= 50:
      level = "Medium 🟡" 
   else:
      level = "Weak 🟢"
   
   print("Your new generated password is:", password)
   print(f"Strength score: {score}% ({level})")
    

if __name__=='__main__':
   main()