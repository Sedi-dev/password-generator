#password generator
#Lesedi Mohale
#24 April 2026

import random
import string

def generator(length):
   
   lower = string.ascii_lowercase 
   upper = string.ascii_uppercase
   digit = string.digits
   symbol = '!@#$%_-/'
   
   pw_list = [random.choice(lower), random.choice(upper), random.choice(digit), random.choice(symbol)]
      
   # combination of each character type
   all_chars = lower + upper + digit + symbol
   
   for _ in range(length - 4): #12(length of password) - 4(current length)
      pw_list.append(random.choice(all_chars))
   
   #shuffle to remove predictable order
   random.shuffle(pw_list)
   
   #convert to string
   password = "".join(pw_list)
          
   return password
   

def main():
   
   length = int(input("Enter password length:\n"))
   
   if length < 4:
      print("Password must be at least 4 characters")
      return  
   
   print("Your new generated password is:", generator(length))   
    

if __name__=='__main__':
   main()