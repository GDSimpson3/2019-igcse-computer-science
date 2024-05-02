# Q02a

from random import * 
# import random
#  Initialise variables

counter = 1
answer = randint(1,10) 
guess =0

#  Print prompt and take guess from user

# print("enter a number from 1 to 10")
guess = int(input("enter a number from 1 to 10: "))

#  Create WHILE loop to check if guess is correct
while guess < answer or guess > answer:
	counter = counter + 1
	if guess > answer:
		print("Guess was too high")
	else:
		print("Guess was too low")
	print("Guess again")
	guess = int(input("enter a number from 1 to 10: "))



#  Report the correct answer to the user and indicate the number of guesses

print(f'You guessed {guess} in {counter} Guesses')