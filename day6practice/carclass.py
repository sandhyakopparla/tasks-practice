class Cars:
    color="white"
    brand="BMW"
    def findMileage(self,li,km):
        return km/li
myCar=Cars()
a1=input("enter color:")
a2=input("enter brand:")
l=int(input("enter the litres:"))
k=int(input("enter the kilometers:"))
mileage=myCar.findMileage(l,k)
myCar.color=a1
myCar.brand=a2
print(myCar.color)
print(myCar.brand)
#printing default values using objects
defaultCar=Cars()
print(defaultCar.color)
print(defaultCar.brand)
print(mileage)



