#Creating a Guessing game program

import random

def generate_random_number(min_value, max_value):
  return random.randint(min_value, max_value)

def play_guessing_game(min_value, max_value):
  random_number = generate_random_number(min_value, max_value)

  num_guesses = 0

  while True:
    guess = int(input("Guess a number between {} and {}: ".format(min_value, max_value)))

    num_guesses += 1

    if guess == random_number:
      print("Congratulations! You guessed the correct number in {} guesses!".format(num_guesses))
      break
    elif guess < random_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")

if __name__ == "__main__":
  min_value = int(input("Enter the minimum value for the random number: "))
  max_value = int(input("Enter the maximum value for the random number: "))

  play_guessing_game(min_value, max_value)
