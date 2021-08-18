class Food:
    def Dosa(self,masaladosa):
        self.masaladosa=masaladosa
        print(self.masaladosa)
class Drink(Food):
    def juice(self,fanta):
        self.fanta=fanta
        print(self.fanta)
class Cool(Drink):
    def Icecream(self,Blackcurrent):
        self.Blackcurrent=Blackcurrent
        print(self.Blackcurrent)
obj=Cool()
obj.Dosa("masaladosa")
obj.juice("fanta")
obj.Icecream("blackcurrent")