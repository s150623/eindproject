# class Chipkaart:
#     def __init__(self):
#         self.code = None
    
#     def initialiseer(self, code):
#         self.code = code
#         print("de chip is geinitialiseerd")
    
#     def gebruik_chip(self):
#         self.code = None
#         print("de chipkaart is gebruikt")

class Chipkaart:
    def __init__(self, naam):
        self.naam = naam
        self.geinitialiseerd = False
    
    def initialiseer(self):
        self.geinitialiseerd = True
        print(f"de chip is geinitialiseerd voor {self.naam}")
    
    # def get_chip(self):
    #     if self.geinitialiseerd:
    #         return True
    #     return False
    
    def gebruik_chip(self):
        self.geinitialiseerd = False
        print("de chipkaart is gebruikt")
        print(f"{self.naam} heeft chip terug gegeven")

    