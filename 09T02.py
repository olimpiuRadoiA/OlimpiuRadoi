


class Book:
    title = 0
    yearOfRelease = 0
    publisher = 0
    genre = 0
    author = 0
    price = 0
    
    def __init__(self, title, yearOfRelease, publisher, genre, author, price):
        self.title = title
        self.yearOfRelease = yearOfRelease
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
        
    def __str__(self):
        return "Cartea " + str(self.title) + " a fost publicata in anul " + str(self.yearOfRelease) + " de editura " + str(self.publisher) + " este o carte reprezentativa a genului " + str(self.genre) + ", autorul cartii este " + str(self.author) + " si o puteti achizitiona la pretul de " + str(self.price)
    
    def getTitle(self):
        return self.title
    
    def getYearOfRelease(self):
        return self.yearOfRelease
    
    def getPublisher(self):
        return self.publisher
    
    def getGenre(self):
        return self.genre
    
    def getAuthor(self):
        return self.author
    
    def getPrice(self):
        return self.price
    
title = "Un baiat numit Craciun"
yearOfRelease = "2021"
publisher = "nemi"
genre = "beletristica"
author = "Matt Haig"
price = "33 lei"

w = Book(title, yearOfRelease, publisher, genre, author, price)
print(w)
        
        
        