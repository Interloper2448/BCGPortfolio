#
# Example file for formatting time and date output
#

from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()

    #### Date Formatting ####
    # print(now.strftime("The year is: %Y %D %A"))
    # print(now.strftime("The year is: %y %d %a"))

    # # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

    # # %c - locale's date and time, %x - locale's date, %X - locale's time
    # print(now.strftime("LocaleDateand time: %c"))
    # print(now.strftime("LocaleDateand time: %C"))
    # print(now.strftime("LocaleDateand time: %x"))
    # print(now.strftime("LocaleDateand time: %X"))
    #### Time Formatting ####
    print(now.strftime("current: %I:%M:%S %p"))
    print(now.strftime("24-hour: %H:%M"))
    print(now.strftime("Don't use: %h:%m"))
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM


if __name__ == "__main__":
    main()
