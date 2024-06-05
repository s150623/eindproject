class Kiezer:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
        self.gestemd = False
    
    def stem(self):                                 
        self.gestemd = True
    
    def get_gestemd(self):
        if self.gestemd:
            return True
        return False

    def __str__(self):
        return f"{self.naam}, {self.leeftijd} jaar oud"
    

# class Kiezer:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.check_gestemd = False  # Instance attribute

#     def stem(self):
#         self.check_gestemd = True


