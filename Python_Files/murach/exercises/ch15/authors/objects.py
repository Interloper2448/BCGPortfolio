class Book:
    def __init__(self, title="", authors=None):
        self.title = title
        self.authors = authors

    def __str__(self):
        return self.title + " by " + str(self.authors)
                
class Author:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        ret = self.firstName + " " + self.lastName
        return ret


class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)
    
    def __str__(self):
        ret = ""
        for author in self.__list:
            ret+= author.firstName + " " + author.lastName
            if len(self.__list) -1 != self.__list.index(author):
                ret += ", "
        return ret

    # define the Author object as the iterator
    def __iter__(self):
        self.__index = -1   # initialize index for each iteration
        return self

    # define the method that gets the next object
    def __next__(self):
        if self.__index >= len(self.__list)-1:
            raise StopIteration()
        author = self.__list[self.__index]
        self.__index += 1
        return author

    @property
    def count(self):
        return len(self.__list)
