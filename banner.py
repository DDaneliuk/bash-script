import sys
import os

"""
Print the startup banner
""" 
def ban():
	print("\033[H\033[J") # Clear the screen
	print("\033[01;31m")
	sys.stdout.write(open("logo.txt", "r").read()[:-1])
	print("\033[00m")
	sys.stdout.write("\n\t  .:[ Banner version 0.0.1 ]:.\n\033[00m\n")
	sys.stdout.write("\t  \n\033[00m")
ban()
# clean screen
def clean():
	print("\033[H\033[J") # Clear the screen

# start game
def game():
	print("Start Game")
	cursor = raw_input("")

# check prompt 
while True:
	try:
		cursor = raw_input("$ ")
		prompt = cursor.split()
		if not prompt:
			continue
		elif prompt[0] == "exit":
			clean()
			print("Bye bye...")
			break
		elif prompt[0] == "ban":
			ban()
		elif prompt[0] == "cls":
			ban()
		elif prompt[0] == "game":
			game()
	except:
		print(" Do you wanna exit? - try"+" exit" )
