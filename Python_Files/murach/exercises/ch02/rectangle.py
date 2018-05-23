#!/usr/bin/env python3

# display a welcome message
print("The Rectangle Program")
print()

# get input from the user
input_length = float(input("Enter the Length:\t\t"))
input_width = float(input("Enter the Width:\t\t"))

# calculate miles per gallon
area = input_length * input_width
peri = input_length * 2 + input_width * 2

# format and display the result
print("Area:\t\t\t\t" + str(area))
print("Perimiter:\t\t\t" + str(peri))
print("\n\rThanks for using the program!")
