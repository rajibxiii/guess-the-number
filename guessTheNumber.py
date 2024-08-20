import random

print("""
      Welcome to the number guessing game!
      I am thinking of a number between 1 and 100.
      """)
difficulty = input ("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 5
if difficulty == 'easy':
     attempts += 5

number = random.randint(1, 100)

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

    attempts -= 1

    if (attempts != 0):
        print (f"Guess again.\nYou have {attempts} attempts remaining.")

    else: break

print ("\nYou've run out of guesses, you lose.")
print (f"The correct answer was {number}")