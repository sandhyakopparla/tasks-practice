class Grandfather:
    def eatfood(self,food):
        self.food=food
        print(self.food)
class Father(Grandfather):
    def drinkcoffee(self,coffee):
        self.coffee=coffee
        print(self.coffee)
class Child(Father):
    def eatchocolates(self,chocolates):
        self.chocolates=chocolates
        print(self.chocolates)
obj=Child()
obj.eatfood("parota")
obj.drinkcoffee("continental")
obj.eatchocolates("munch")