class Parent:
     def eat(self):
          print("he will eat")
class Child(Parent):
     def drink(self):
          print(" he will drink")
obj= Child()
obj.eat()
obj.drink()