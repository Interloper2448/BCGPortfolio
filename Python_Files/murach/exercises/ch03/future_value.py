#!/usr/bin/env python3

def filterMonInp(statement):
    while True:
        inp = float(input(statement))
        if inp <= 0:
            print("Entry must be greater than 0")
        else:
            return inp

def filterIntreInp(statement):
    while True:
        inp = float(input(statement))
        if inp <= 0:
            print("Entry must be greater than 0")
        elif inp > 15:
            print("Entry must be less than or equal to 15")
        else:
            return inp

def filterYearsInp(statement):
    while True:
        inp = int(input(statement))
        if inp <= 0:
            print("Entry must be greater than 0 and less than or equal to 50")
        elif inp > 50:
            print("Entry must be greater than 0 and less than or equal to 50")
        else:
            return inp


# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = filterMonInp("Enter monthly investment:\t")
    yearly_interest_rate = filterIntreInp("Enter yearly interest rate:\t")
    years = filterYearsInp("Enter number of years:\t\t")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        if i % 12 == 11:
            print("Year = ", round(i/12), " Future Value = ", round(future_value, 2))

    # display the result
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
