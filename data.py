import random
from unittest import result
from chipkaart import Chipkaart
from kiezer import Kiezer
from stemcomputer import Stemcomputer1, Stemcomputer2, Stemcomputer3
from scanner import Scanner
from stembus import Stembus
from partij import Partij


class data:

    def __init__(self):
        self.totaal = 0
        self.kiezers_lijst = []
        self.De_goede = Partij("De Goede")
        self.De_slechte = Partij("De Slechte")
        self.De_groene = Partij("De Groene")
        self.De_grappige = Partij("De Grappige")
        self.De_oliebollen = Partij("De Oliebollen")
        self.alle_partijen_zonder_kandidaten = [self.De_goede, self.De_slechte, self.De_groene, self.De_grappige, self.De_oliebollen]
        self.alle_partijen = [self.De_goede, self.De_slechte, self.De_groene, self.De_grappige, self.De_oliebollen]
        self.chipkaarten_lijst = []
        self.STEMCOMPUTERS = [Stemcomputer1, Stemcomputer2, Stemcomputer3]
        self.stembus = Stembus()
        self.scanner = Scanner(self.stembus)

    def initialiseer(self):
        self.lijst_namen()
        self.partijen()
        # self.print_partijen()
        self.chipkaarten()

    def Namen_generator(self):  # random namen genereren
        voornaam = ("Janneke", "Mohammed", "John", "Thomas", "Diego", "Cid", "Jack", "Sarah", "Emilia", "Kemo")
        achternaam = ("Cena", "Pis", "Ali", "Maene", "Neji", "Costa", "Vermeulen", "Mortimer", "De Mets", "Kagenou")

        return random.choice(voornaam) + " " + random.choice(achternaam)                                    # voornaam met achternaam toevoegen

    def leeftijd_generator(self):
        leeftijd = random.randrange(18, 91)
        return leeftijd

    def lijst_namen(self):  # lijst aanmaken met alle kiezers met hun leeftijd
        for _ in range(1200):
            persoon = Kiezer(self.Namen_generator(), self.leeftijd_generator())
            self.kiezers_lijst.append(persoon)                                                   # alle gegevens worden opgeslagen in een lege lijst genaam kiezers_lijst

    def partijen(self):                                                                             # hier worden # de kandidaten toegevoegd aan een willekeurige partij met elk partij die 10 kandidaten bevatten
        for partij in self.alle_partijen:                                                        # elke kandidaat wordt toegevoegd aan een partij met 10 kandidaten
            for _ in range(10):
                partij.kandidaat_toevoegen(random.choice(self.kiezers_lijst))





        # for i, lst in enumerate(self.alle_partijen, start=1):                                                       #test om te zien dat elk partij 10 kandidaten bevat
        #     print(f"List {i}: {partij}")

        # self.lijst_namen()
        # global partijen_met_kandidaten

        # partijen_met_kandidaten = {partij: [] for partij in self.namen_partijen}                                    #vorige code
        # for partij in self.namen_partijen:
        #     for _ in range(10):
        #         kandidaat = random.choice(self.kiezers_lijst)
        #         partijen_met_kandidaten[partij].append(kandidaat)
        #         self.kiezers_lijst.remove(kandidaat)                                                                      # herhaling vermijden

    # def print_partijen(self):
    #     for i, partij in enumerate(self.alle_partijen, start=1):
    #         print(f"Party {i}:")
    #         for persoon in partij:                                                                               #test om te zien dat elke partij 10 kandidaten bevat
    #             print(f"Name: {persoon.naam}, Age: {persoon.leeftijd}")
    #         print("\n")

    def chipkaarten(self):  # 60 chipkaarten worden met deze functie gemaakt
        for _ in range(60):
            chipkaart = Chipkaart(_)
            self.chipkaarten_lijst.append(chipkaart)

    def stemproces(self):
        for kiezer in self.kiezers_lijst:
            if not kiezer.gestemd:                                                              # als kiezer nog niet heeft gestemd dan kiest die een partij :: Kiezer hier is de class in kiezer.py!
                if random.choice([True, False]):                                                   # als True dan wordt er gekozen voor een partij anders voor een kandidaat
                    gebruik = Chipkaart(kiezer)
                    gebruik.initialiseer()
                    keuze = random.choice(self.alle_partijen_zonder_kandidaten)
                    print(f"{kiezer} koos {keuze}")
                    kiezer.stem()
                    self.totaal += 1
                    gekozen_Stemcomputer = random.choice(self.STEMCOMPUTERS)
                    gekozen = gekozen_Stemcomputer("USB1", gebruik)
                    stembiljet = gekozen.stem_verwerking(kiezer, keuze, "partij")
                    if stembiljet:
                        self.scanner.scan(stembiljet)
                else:
                    gebruik = Chipkaart(kiezer)
                    gebruik.initialiseer()
                    partij = random.choice(self.alle_partijen_zonder_kandidaten)                              #partij kiezen
                    keuze = partij.random_kandidaten()
                    kiezer.stem()
                    self.totaal += 1
                    gekozen_Stemcomputer = random.choice(self.STEMCOMPUTERS)
                    gekozen = gekozen_Stemcomputer("USB1", gebruik)
                    stembiljet = gekozen.stem_verwerking(kiezer, keuze, "kandidaat")
                    if stembiljet:
                        self.scanner.scan(stembiljet)

    def toon_resultaten(self):
        resultaten_lijst = self.stembus.verwerking_stemmen_lijstem()
        print("\nStemmen op partijen:")
        for keuze, aantal in resultaten_lijst.items():
            print(f"{keuze}: {aantal} stemmen")

        resultaten_kandidaten = self.stembus.verwerking_stemmen_kandidaten()
        print("\nStemmen op kandidaten:")
        for keuze, aantal in resultaten_kandidaten.items():
            print(f"{keuze}: {aantal} stemmen")

        print(f"\nTotaal aantal stemmen: {self.totaal}")

 


# instance = data()
# nee = instance.initialiseer()  # een test om stemproces te testen
# yes = instance.stemproces_lijstem()
# instance.toon_resultaten()

#     def test(self):
#         #  keuze = random.choice(self.namen_partijen)
#         #  print(keuze)
#         gekozen_Stemcomputer = random.choice(self.STEMCOMPUTERS)
#         gekozen = gekozen_Stemcomputer()                                                                                 #om bepaalde dingen te testen                       
#         print(gekozen.testing()

# instance = data()
# yes = instance.stemproces()