
#Salary calculator
'''
Collect rate/hr and ideal number of hours
If overtime is experieced, calculate number of extra hours and rate for pay
Output the total amount to be paid as salary
'''
def f(data):
    try:
        data = float(data)
    except:
     print("Invalid input")

    return data

fhrs = f(input("\nHow many hours did you work this month? \n"))
frate = f(input("What is the pay rate per hour? \n"))
fmaxhrs = f(input("What is the maximum number of hours a worker should work? \n"))

try:
    if (fhrs > fmaxhrs):
        print("\nYou worked overtime!")
        ovt = ((fhrs - fmaxhrs) * (frate * 0.5)) + (fmaxhrs * frate)
        print(f"\nYour pay for this month is {ovt}\n")

    elif (fhrs == fmaxhrs):
        print("\nYou were very effective this month!\n")
        pay = (fhrs * frate)
        print(f"Your pay for this month is {pay}\n")

    elif (fhrs < fmaxhrs):
        print("\nYou have done well this month. You can do better next month to get a higher pay.")
        lpay = (fhrs * frate)
        print(f"\nYour pay for this month is {lpay}\n")

    else:
        print("Kindly input the number of hours you worked this month next time.\n")
except:
    print("\nSorry, I can't come up with a salary for you. Ensure the values you input are in digits only.\n")