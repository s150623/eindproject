from usbstick import USBStick
from stembiljet import Stembiljet

class Stembus:
    def __init__(self):
        self.stembiljetten = []
    
    def initialiseer(self, code):
        self.code = code
        USBStick(code)
        print("de stembus is geinitialiseerd")
    
    def toevoeging_stembiljet(self, stembiljet):                        #hier word een stembiljet toegevoegd aan de lijst self.stembiljetten
        self.stembiljetten.append(stembiljet)
        return print("stembiljet werd toegevoegd aan de stembus")
    
    def verwerking_stemmen_lijstem(self):
        resultaten = {}
        for stembiljet in self.stembiljetten:
            if stembiljet.soort_keuze == "partij":                #als de keuze van het stembiljet een partij is dan wordt die toegevoegd aan de resultaten
                keuze = stembiljet.Keuze
                if keuze in resultaten:
                    resultaten[keuze] += 1                          #als er al een stem is gemaakt op die keuze dan wordt er +1 toegevoegd
                else:
                    resultaten[keuze] = 1                           #als er geen stem is gemaakt op een bepaalde keuze is die gelijk aan 1
        return resultaten
    
    def verwerking_stemmen_kandidaten(self):
        resultaten = {}
        for stembiljet in self.stembiljetten:
            if stembiljet.soort_keuze == "kandidaat":
                keuze = stembiljet.Keuze
                if keuze in resultaten:
                    resultaten[keuze] += 1
                else:
                    resultaten[keuze] = 1
        return resultaten
    
