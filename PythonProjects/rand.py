#Takes input of a range of numbers
val = input("Insert numbers (e.g: 1, 2, 3, 4,...): ").split(", ")

#print out the largest number
print(max(val))

#prints out the smallest number
print(min(val))

#converts the strings in the list to integers
xxx = list(map(int, val))

#prints the average value of the numbers
print(sum(xxx)/len(xxx))



