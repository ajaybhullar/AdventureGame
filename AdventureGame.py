#!/usr/bin/env python
import random

#This method allows you to make a yes or no decision
def yesorno(query):
	invalidInput = True
	yes = ['yes','y']
	no = ['no','n']

	while invalidInput:
		choice = input('%s[Y/N]\n' % query).lower()
		if choice in yes:
			return True
		elif choice in no:
			return False
		else:
			print("Please enter only any of the following: Yes, yes, y, No, no, n")

#This method is used to choose one of the options given in a room, there will neber be more than 5 options
def choose(numOptions):
	choice = 0
	choices = ['1', '2', '3', '4', '5']
	while choice < 1:
		answer = input("\nPick a number from 1 to " + str(numOptions) + " to make your choice. ")
		if answer in choices and int(answer) <= numOptions:
			return int(answer)
		else: 
			print("Invalid input, please pick a number from 1 to " + str(numOptions))
			choice = 0

#This is the room you start in
def intro():
	print("\nYou enter the first room. Inside the room there are two doors side by side. ")
	print(" 1. Do you enter the right door? ")
	print(" 2. Do you enter the left door? ")
	print(" 3. Do you turn around and leave through the door you just came in? ")
	choice = choose(3)
	if choice == 1:
		print("\nYou decide to walk through the door on the right. ")
		rightDoor()
	elif choice == 2:
		print("\nYou decide to walk through the door on the left. ")
		leftDoor()
	elif choice == 3:
		print("\nYou decide to turn around and leave")
		theExit()

#This is the first room again but from the viewpoint of re-entering it from the door on the left
def firstRoom():
	print("You re-enter the first room. Inside the room there are two doors side by side. ")
	print(" 1. Do you enter the right door? ")
	print(" 2. Do you decide to re-enter the left door? ")
	print(" 3. Do you decide to try and leave through the door that led to the first room? ")
	choice = choose(3)
	if choice == 1:
		print("\nYou decide to walk through the door on the right. ")
		rightDoor()
	elif choice == 2:
		print("\nYou decide to walk through the door on the left. ")
		leftDoor()
	else:
		print("\nYou decide to leave. ")
		theExit()

#This is the door on the left of the first room
def leftDoor():
	print("Inside the room you find a note. ")
	print("The note reads \"The next door is locked by a code, a single number between 1 and 100, can you guess what it is?\"")
	print("1. Try to guess the number.")
	print("2. Turn around and leave.")

	choice = choose(2)
	if choice ==1:
		unlocked = guessingGame()
	if choice ==2:
		firstRoom()

	if unlocked:
		if yesorno("Do you want to go through the door? "):
			theHallway()
		else:
			print("You did not go through the door. You now have two choices: ")
			print("1. Reset the code on the lock and play again ")
			print("2. Go back through the door which led to this room ")
			choice = choose(2)
			if choice == 1:
				guessinggame()
			else:
				firstRoom()

#This is the guessing game encountered in the left room from the first door
def guessingGame():
	code = random.randint(1,100)
	guess = 0
	unlocked = False
	while guess != code:
		guess = input("Choose a number between 1 and 100. ")
		if( int(guess) < 1 or int(guess) > 100 ):
			print('%s is an invalid guess, please pick a number between 1 and 100, or enter No to quit ' % guess)
		else:
			if(int(guess) > code):
				print("The number you have guessed is too high\n" )
			elif(int(guess) < code):
				print("The number you have guessed is too low\n" )
			elif(guess.lower() == 'no'):
				print("You step away from the door that is locked. ")
				unlocked = False
				return unlocked
			else:
				print("You have unlocked the door! ")
				unlocked = True
				return unlocked

#This is the door on the right from the first room
def rightDoor():
	print("the right door under construction! ")

def theExit():
	print("the exit is under construction! ")

def theHallway():
	print("this hallway is under construction! ")

print("Welcome to the game!\nEach room requires you make a choice, and each choice has an outcome\nKeep playing until the end! ")
choice = yesorno("Do you wish to play? ")

if choice:
	intro()
else:
	exit(1)
