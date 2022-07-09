

'''
This program helps convert from miles to kilometers
By fetching miles value from user and storing in var miles
Multiplying the value of miles by 1.60934 and store value in kilometer
print value of Kilometer
'''

miles = input("How many miles do you want to convert to kilometers? \n")
miles = int(miles)
kilometer = miles * 1.60934
print ("That is {}km".format (kilometer))