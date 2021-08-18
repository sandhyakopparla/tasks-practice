class Trees:
    def Neam(self,Bitter):
        self.Bitter=Bitter
        print(self.Bitter)
class Smallplants(Trees):
    def Tulasi(self,peppery):
        self.peppery=peppery
        print(self.peppery)
class Flowerplants(Smallplants):
    def Jasmine(self,smell):
        self.smell=smell
        print(self.smell)
obj=Flowerplants()
obj.Neam("Neam is bitter taste")
obj.Tulasi("peppery taste")
obj.Jasmine("smells good")