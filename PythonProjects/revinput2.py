#!/usr/bin/python3
'''
This program checks if a string input is a palindrome
Returns true if it is, else, false

'''

def pali(s):
	str = ""
	for i in s:
		str = i + str
	if str == s:
		print("Your input is a palindrome!")
		return True
	else:
		print(f"The word the inserted is {s}\nThe reverse is {str}")
		return False
	return str

Insert = input("Insert a word or sentence: ")
pali(Insert)
