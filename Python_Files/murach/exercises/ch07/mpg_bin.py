#!/usr/bin/env python3
import csv
import pickle
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
    

    trips = read_file()
    list_stuff()

    more = "y"
    while more.lower() == "y":
        # list_stuff()
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        stats = []
        stats.append(miles_driven)
        stats.append(gallons_used)
        stats.append(mpg)
        trips.append(stats)

        # Write
        write_file(trips)
        # with open(getDir("gasUsed.bin"), "ab") as file:
        #     pickle.dump(stats, file)

        more = input("More entries? (y or n): ")

    print("Bye")

def getDir(file):
    myFile = []
    myFile = path.split(__file__)
    return myFile[0] + "\\" + file

def write_file(stats):
    with open(getDir("trips.bin"), "wb") as file:
        pickle.dump(stats, file)

def read_file():
    with open(getDir("trips.bin"), "rb") as file:
        trips = pickle.load(file)
    return trips

def list_stuff():
    trips = read_file()
    for i in range(len(trips)):
        trip = trips[i]
        print(trip[0], "\t\t", trip[1], "\t\t", trip[2])

if __name__ == "__main__":
    main()
    list_stuff()
