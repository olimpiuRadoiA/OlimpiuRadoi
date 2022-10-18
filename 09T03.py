class Stadium:
    name = 0
    dateOfOpening = 0
    country = 0
    city = 0
    capacity = 0
    
    def __init__(self, name, dateOfOpening, country, city, capacity):
        self.name = name
        self.dateOfOpening = dateOfOpening
        self.country = country
        self.city = city
        self.capacity = capacity
        
    def __str__(self):
        return "Stadionul " + str(self.name) + " deschis in anul " + str(self.dateOfOpening) + " se afla in " + str(self.country) + " in orasul " + str(self.city) + " si are o capacitate " + str(self.capacity)
    
    def getName(self):
        return self.name
    
    def getDateOfOpening(self):
        return self.dateOfOpening
    
    def getCountry(self):
        return self.country
    
    def getCity(self):
        return self.city
    
    def getCapacity(self):
        return self.capacity
    
name = "WEMBLEY"
dateOfOpening = "2007"
country = "England"
city = "London"
capacity = "90.000 de locuri"

w = Stadium(name, dateOfOpening, country, city, capacity)
print(w)