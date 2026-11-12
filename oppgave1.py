import random
 
print("welcome to the 'Guess the number game'!")
print("I'm thinking of a number between 1 and 10. Try guess what number i'm thinking of!")
 
Right_Number = random.randint(1, 10)
 
while True:
    # Be brukeren om en gjetning
    guess = int(input("Write a number between 1 and 10: "))
 
    if guess == Right_Number:
        print("Congrats! You guessed right.")
        print("Thank you for playing!")
        break
    else:
        print("Wrong! Try guessing a different number.")
    if guess <= Right_Number:
        print ("The number is higher!")
    if guess >= Right_Number:
        print ("The number is lower!")
        