class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name


class Media(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, format=""):
        self.format = format
        Product.__init__(self, name, price, discountPercent)
        

    # def getDiscription(self):
    #     return Product.getDescription(self)


class Book(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, author="", format="Hardcover"):
        self.author = author
        Media.__init__(self, name, price, discountPercent, format)
        # Book("The Big Short", 15.95, 34, "Michael Lewis", "Ebook"))  # ,

    def getDescription(self):
        return Media.getDescription(self) + " by " + self.author


class Album(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, author="", format="cassette"):
        Media.__init__(self, name, price, discountPercent, format)
        self.author = author

    def getDescription(self):
        return Media.getDescription(self) + " by " + self.author


class Movie(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, year=0, format="DVD"):
        Media.__init__(self, name, price, discountPercent, format)
        self.year = year

    def getDescription(self):
        return Media.getDescription(self) + " (" + str(self.year) + ")"
