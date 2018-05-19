import random


class Die:
    def __init__(self):
        self.__value = Die.roll(self)

    @property
    def value(self):
        return self.__value

    @property
    def image(self):
        val = self.__value
        if val == 1:
            img = "Your Roll: " + str(val) + "\n _____ \n" + "|     |\n" + "|  o  |\n" + "|_____|"
            return img
        elif val == 2:
            img = "Your Roll: " + str(val) + "\n _____ \n" + "|o    |\n" + "|     |\n" + "|____o|"
            return img
        elif val == 3:
            img = "Your Roll: " + str(val) + "\n _____ \n" + "|o    |\n" + "|  o  |\n" + "|____o|"
            return img
        elif val == 4:
            img = "Your Roll: " + str(val) + "\n _____ \n" + "|o   o|\n" + "|     |\n" + "|o___o|"
            return img
        elif val == 5:
            img = "Your Roll: " + str(val) + "\n _____ \n" + "|o   o|\n" + "|  o  |\n" + "|o___o|"
            return img
        elif val == 6:
            img = "Your Roll: " + str(val) + "\n _____ \n" + "|o   o|\n" + "|o   o|\n" + "|o___o|"
            return img

    @value.setter
    def value(self, value):
        if value < 1:
            raise ValueError("Die can't be less than 1.")
        elif value > 6:
            raise ValueError("Die can't be greater than 6.")
        else:
            self.__value = value

    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value


class Dice:
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple

    def rollAll(self):
        for die in self.__list:
            die.roll()

    def getTotal(self):
        tot = 0
        for d in self.__list:
            tot += d.value
        return tot