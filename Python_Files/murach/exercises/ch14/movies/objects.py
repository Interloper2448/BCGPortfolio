
class Movie:
    def __init__(self,name="",year=0):
        self.name = name
        self.year = year

    def getStr(self):
        return self.name + " ("+str(self.year)+")"



def main():
    mov = Movie()
    mov.name = "The Moleman"
    mov.year = 2050
    print(mov.name, mov.year)

if __name__ == "__main__":
    main()
