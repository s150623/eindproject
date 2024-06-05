from stembus import Stembus

class Scanner:
    def __init__(self, stembus):
        self.stembus = stembus
    
    def scan(self, stembiljet):
        self.stembus.toevoeging_stembiljet(stembiljet)
        print("stembiljet werd gescand")
        print("stembiljet is geldig")
    
