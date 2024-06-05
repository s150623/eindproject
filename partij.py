import random


class Partij:
    def __init__(self, naam):
        self.naam = naam
        self.kandidaten = []

    def kandidaat_toevoegen(self, kandidaten):
        self.kandidaten.append(kandidaten)

    def __str__(self):
        return self.naam
    
    def random_kandidaten(self):
        return random.choice(self.kandidaten)