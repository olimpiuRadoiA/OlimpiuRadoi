


class Car:
    model = ''
    yearOfRelease = ''
    manufactured = ''
    engineCapacity = ''
    color = ''
    price = ''
    
    def __init__(self, model, yearOfRelease, manufactured, engineCapacity, color, price):
        self.model = model
        self.yearOfRelease = yearOfRelease
        self.manufactured = manufactured
        self.engineCapacity = engineCapacity
        self.color = color
        self.price = price
        
    def __str__(self):
        return "modelul de masina: " + self.model + " din anul: " + self.yearOfRelease + " fabricat " + self.manufactured + " cu capacitatea motorului de:  " + self.engineCapacity + " de culoare:  " + self.color + " la pretul de:  " + self.price 
    
    def getModel(self):
        return self.model
    
    def getYearOfRealese(self):
        return self.yearOfRelease
    
    def getManufactured(self):
        return self.manufactured
    
    def getEngineCapacity(self):
        return self.engineCapacity
    
    def getColor(self):
        return self.color
    
    def getPrice(self):
        return self.price
    
model = input("modelul de masina: ")
yearOfRelease = input("din anul: ")
manufactured = input("fabricat: ")
engineCapacity = input("oras resedinta: ")
color = input("de culoare: ")
price = input("adresa completa: ")    

    
w = Car(model, yearOfRelease, manufactured, engineCapacity, color, price)
print(w)