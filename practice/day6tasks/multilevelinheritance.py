class Parent:
      def eat(self):
          print("he will eat")
class Child(Parent):
      def drink(self):
          print("he will drink")
class Child2(Child):
      def play(self):
          print("he will play")
ob = Child2()
ob.eat()
ob.drink()
ob.play()