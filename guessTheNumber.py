import logos
import random

print (logos.guessdnumber)
print("""
      Welcome to the number guessing game!
      I am thinking of a number between 1 and 100.
      """)
difficulty = input ("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 5
if difficulty == 'easy':
     attempts += 5

number = random.randint(1, 100)
print (number)

print (f"You have {attempts} attempts remaining to guess the number")

while attempts > 0:
    guess = int(input ("Make a guess: "))

    if guess == number:
          print (f"You got it! The correct answer was {number}")
          break
    else:
        if guess >= number+10:
            print ("Too high.")
        elif guess <= number-10:
          print ("Too low.")

        print (f"Guess again.\nYou have {attempts-1} attempts remaining.")
 
    attempts -= 1

    if (attempts == 0):
        print ("You've run out of guesses, you lose.")
        print (f"The correct answer was {number}")