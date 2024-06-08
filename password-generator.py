import random
import string


print(f"Welcome to Password Generator app.")
user=int(input("how many Characters do you want in your password: "))

def passwordGenerator(user):
    if(user>=4):
         
         capitalLetter=string.ascii_uppercase
         smallLetter=string.ascii_lowercase
         digits=string.digits
         specialChar=string.punctuation


         combineLetter=capitalLetter+smallLetter+digits+specialChar
         password=[


            random.choice(capitalLetter),
            random.choice(smallLetter),
            random.choice(digits),
            random.choice(specialChar)
        ]

         password=password+random.choices(combineLetter,k=user-4)
         random.shuffle(password)
         return  "".join(password)
    
    else: 
        print(f"Please enter a number greater than {user}! ")

print(passwordGenerator(user))