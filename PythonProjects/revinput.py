#!/usr/bin/python3
'''
This program print the reverse of its string input

'''

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

intake = input("Insert a word: \n")
rev = reverse(intake)
print(f"The word you inserted is {intake} and the reverse is {rev}")
