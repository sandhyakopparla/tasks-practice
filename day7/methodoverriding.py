class Car:
    def audi(self):
        print("Red")
class BMW(Car):
    def color(self):        #in methodoveriding we can use same property as parent class like in car we have usen color in BMW also we have usen color
        print("white")
obj=BMW()
obj.color()
obj.audi()