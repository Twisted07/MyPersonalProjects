#!/bin/user/python3

'''
This programs automatically replies basic chats
How are you? - I'm doing great, you?
Good morning - Good morning
How much && "cards" - print(card pricelist)
Good afternoon - Good afternoon
Hello - Hello $user
Hi - Hi
Good night - Sweet dreams
'''
greetingCardsPricelist = "A4 size cards: /#7000,\n" "A3 size cards: /#15000\n"
greeting = input("")

if (greeting == "Hello") or (greeting == "Hi") or (greeting == "hi") or (greeting == "hello"):
	user = input("What's your name please? ")
	print(f"{greeting} {user}. How are you doing?")
	response = input("")

	if (response[-4:] == "you?") or (response[-4:] == "You?") or (response[-4:] == " you") or (response[-4:] == " You"):
		print("I'm doing great too. Thank you.")
	else:
		print("Okay!")

elif (greeting[:8] == "How much"):
	request = input("\n\nWhich of our pricelists would you like to see?\n\n Greeting Cards\n Gift Boxes\n Business Flashcards (Thank you cards)\n")

	if (request == "Greeting Cards") or (request == "greeting cards") or (request == "Greeting cards"):
		print(f"Here's {request} pricelist\n {greetingCardsPricelist}")
	else:
		print("Please choose from the list and type it the way it is on the menu. Thank you!")
else:
	print("Hello Dear! How may I be of service to you?\n")
