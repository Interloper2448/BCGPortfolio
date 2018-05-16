#!/usr/bin/env python3
import csv
from os import path


def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))
        if miles_driven > 0:
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue


def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))
        if gallons_used > 0:
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue


def main():
    # display a welcome message
    print("\n********************************")
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        reader()
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        stats = [str(miles_driven), str(gallons_used), str(mpg)]
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        # Write
        with open(getDir("gasUsed.csv"), "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(stats)

        more = input("More entries? (y or n): ")

    print("Bye")


def getDir(file):
    myFile = []
    myFile = path.split(__file__)
    return myFile[0] + "\\" + file


def reader():
    print("*************************")
    data = []
    with open(getDir("gasUsed.csv"), "r", newline="") as files:
        reader = csv.reader(files)
        for row in reader:
            data.append(row)
    print("Distance\t Gallons\t MPG")
    for record in data:
        print(record[0],"\t\t",record[1],"\t\t",record[2])
    print()
    


if __name__ == "__main__":
    main()
    reader()
