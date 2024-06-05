from kiezer import Kiezer
from stembus import Stembus
from stembiljet import Stembiljet
from scanner import Scanner
from usbstick import USBStick
from data import data

# stembus = Stembus()

# Scanner = Scanner(stembus)

# stembiljet1 = Stembiljet("Kiezer1", "Keuze1", "Kandidaat1")
# stembiljet2 = Stembiljet("poep", "zemmers", "de hoer")                                        #stembus checken
# stembiljet3 = Stembiljet("poep", "zemmers", "de hoer")

# Scanner.scan(stembiljet1)
# Scanner.scan(stembiljet2)
# Scanner.scan(stembiljet3)
# Scanner.print_resultaten()

# USB = USBStick("7812")
# Stemcomputer = Stemcomputer(USB)
# kiezer = Kiezer("JEFFKE", "23")                                       #stemcomputer checken
# Stemcomputer.stem_verwerking(kiezer, "jommeke")




# from data import data
#
# # Initialiseer het kiessysteem
# kiessysteem = data()
# kiessysteem.initialiseer()
#
# # Simuleer het stemproces
# kiessysteem.stemproces()
#
# # Toon de resultaten
# kiessysteem.toon_resultaten()

def main():
    instances = Stembus()
    instances.initialiseer(56745322)
    instance = data()
    instance.initialiseer()
    instance.stemproces()
    instance.toon_resultaten()


if __name__ == "__main__":
    main()