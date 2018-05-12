#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
    # DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    # today = date.today()
    # print("Today's Date is: ", today)
    # # print out the date's individual components
    # print("Date components: ", today.day, today.month, today.year)
    # # retrieve today's weekday (0=Monday, 6=Sunday)
    # print("Today's weekday is: ", today.weekday())
    # days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
    # print("Which is a ", days[today.weekday()], sep="")

    # DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print(today)
    # Get the current time
    t = datetime.time(today)
    print(t)


if __name__ == "__main__":
    main()
