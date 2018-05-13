#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gas_price = float(input("Enter the current cost of gas:\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
gas_cost = round(gallons_used * gas_price,2)
mile_cost = round(gas_cost/miles_driven,1)
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total cost of gas:\t\t",gas_cost)
print("Total cost per mile:\t\t", mile_cost)
print("Bye")


