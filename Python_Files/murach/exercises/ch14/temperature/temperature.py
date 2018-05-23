
class Temp:
    def __init__(self):
        self.__fahr = 32
        self.__cels = 0

    def set_celsius(self, celsius):
        self.__cels = celsius
        self.__fahr = celsius * 9/5 + 32

    def set_fahrenheit(self, fahrenheit):
        self.__fahr = fahrenheit
        self.__cels = (fahrenheit - 32) * 5/9

    def get_celsius(self):
        return round(self.__cels, 2)

    def get_fahrenheit(self):
        return round(self.__fahr, 2)


# def to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius


# def to_fahrenheit(celsius):
#     fahrenheit = celsius * 9/5 + 32
#     return fahrenheit

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module


def main():
    # for temp in range(0, 212, 32):
    #     holder = Temp()
    #     holder.set_fahrenheit(temp)
    #     print(holder.get_fahrenheit(), "Fahrenheit equals", holder.get_celsius(),
    #           "Celsius")
    # print()
    # for temp in range(0, 100, 20):
    #     holder = Temp()
    #     holder.set_celsius(temp)
    #     print(holder.get_celsius(), "Celsius equals", holder.get_fahrenheit(),
    #           "Fahrenheit")

    for temp in range(0,100,5):
        holder = Temp()
        holder.set_celsius(temp)
        print(holder.get_celsius(),"Celcius == ",holder.get_fahrenheit(),"Fahrenheit")


# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()
