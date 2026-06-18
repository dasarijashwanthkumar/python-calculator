import random

print("=== NUMBER GUESSING GAME ===")
num = random.randint(1,50)
print("\nEnter Number Between (1-50)\n")

while True:
    
    guessnum = int(input("Enter Your Number :"))

    if guessnum < 1 or guessnum > 50 :
        print("Invalid! Enter Number Between (1-50) ")
        continue

    if guessnum < num:
        print("Your Number is Lower")
    elif guessnum > num:
        print("Your Number is Higher")   
    else:
        print("CONGRATS! YOU GUESSED CORRECTLY")  
        break    
