#!/usr/bin/env python3


while True:
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    # get input from the user
    miles_driven = float(input("Enter miles driven:\t\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t\t"))
    gallon_price = float(input("Enter cost per gallon:\t\t\t"))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif gallon_price <= 0:
        print("The price of a gallon of gas must be greater than 0")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        print("\nMiles Per Gallon:\t\t\t", mpg, sep="")
        # Total Gas cost
        gas_cost = round(gallons_used * gallon_price, 1)
        print("Cost of used gas:\t\t\t", gas_cost, sep="")
        # Cost per mile
        mile_cost = round(gas_cost/miles_driven, 1)
        print("The total cost per mile:\t\t", mile_cost, sep="")

    inp = input("\n\rGet entries for another trip [y/n]?\t").lower()
    if inp == "n":
        break
print()
print("Bye")
