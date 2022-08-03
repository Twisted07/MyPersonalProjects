
class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, new_time):
        add_time = Time()
        #Add seconds and increment minute if seconds > 60
        if (self.second + new_time.second) >= 60:
            self.minute += 1
            add_time.second = (self.second + new_time.second) - 60
        else:
            add_time.second = self.second + new_time.second
        #Add minutes and increment hour if minutes > 60
        if (self.minute + new_time.minute) >= 60:
            self.hour += 1
            add_time.minute = (self.minute + new_time.minute) - 60

        else:
            add_time.minute = self.minute + new_time.minute

        #Add Hour and correct if > 24
        if (self.hour + new_time.hour) > 24:
            add_time.hour = (self.hour + new_time.hour) - 24

        else:
            add_time.hour = self.hour + new_time.hour

        return add_time

def main():
    hr1 = int(input("Insert first hour value: "))
    min1 = int(input("Insert first minute value: "))
    sec1 = int(input("Insert first second value: "))
    time1 = Time(hr1, min1, sec1)

    hr2 = int(input("\nInsert second hour value: "))
    min2 = int(input("Insert second minute value: "))
    sec2 = int(input("Insert second second value: "))
    time2 = Time(hr2, min2, sec2)

    print(f"\nThe first time is {time1}")

    print(f"The second time is {time2}\n")
    print(f"The new time is {time1 + time2}hrs")
main()