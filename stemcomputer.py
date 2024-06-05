
from chipkaart import Chipkaart
from stembiljet import Stembiljet


class Stemcomputer1:
    def __init__(self, usbstick, chipkaart):
        self.name = "stemcomputer1"
        self.usbstick = usbstick
        self.chipkaart = chipkaart
        

    def stem_verwerking(self, kiezer, keuze, soort_keuze):
        if kiezer.get_gestemd():
            if self.chipkaart.geinitialiseerd:
                self.chipkaart.gebruik_chip()
                stembiljet = Stembiljet(kiezer, keuze, soort_keuze)
                return stembiljet
        return None
    
#     def __init__(self):
#         self.name = "stemcomputer1"
#     def testing(self):                                                                            #test om te zien dat er een random stemcomputer wordt gekozen
#         return f"ik ben {self.name}"

class Stemcomputer2:
    def __init__(self, usbstick, chipkaart):
        self.name = "stemcomputer2"
        self.usbstick = usbstick
        self.chipkaart = chipkaart
    
    def stem_verwerking(self, kiezer, keuze, soort_keuze):
        if kiezer.get_gestemd():
            if self.chipkaart.geinitialiseerd:
                self.chipkaart.gebruik_chip()
                stembiljet = Stembiljet(kiezer, keuze, soort_keuze)
                return stembiljet
        return None
    
    # def __init__(self):
    #     self.name = "stemcomputer2"
    # def testing(self):                                                                        #test om te zien dat er een random stemcomputer wordt gekozen                                           
    #     return f"ik ben {self.name}"

class Stemcomputer3:
    def __init__(self, usbstick, chipkaart):
        self.name = "stemcomputer3"
        self.usbstick = usbstick
        self.chipkaart = chipkaart

    def stem_verwerking(self, kiezer, keuze, soort_keuze):
        if kiezer.get_gestemd():
            if self.chipkaart.geinitialiseerd:
                self.chipkaart.gebruik_chip()
                stembiljet = Stembiljet(kiezer, keuze, soort_keuze)
                return stembiljet
        return None
    
    # def __init__(self):
    #     self.name = "stemcomputer3"
    # def testing(self):                                                                    #test om te zien dat er een random stemcomputer wordt gekozen               
    #     return f"ik ben {self.name}"



# instance = Stemcomputer1("USB1")
# kiezer1 = Kiezer("Kiezer1", 25)
# yes = instance.stem_verwerking(kiezer1, "Partij1")