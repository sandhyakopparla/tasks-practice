class Addition:
    def add2numbers(self,a,b):
        return a+b
class Subtract:
    def sub2numbers(self,a,b):
        return a-b
class Multiply:
    def mul2numbers(self,a,b):
        return a*b
class Calculator(Addition,Subtract,Multiply):
    pass
obj=Calculator()
n1=int(input("enter the value:"))
n2=int(input("enter the value:"))
print(obj.add2numbers(n1,n2))
print(obj.sub2numbers(n1,n2))
print(obj.mul2numbers(n1,n2))
# print(issubclass(Calculator,Addition))#it is used because if we want to check the calculator is subclass of Addition
# print(issubclass(Calculator,Subtract))
# print(issubclass(Calculator,Multiply))
# print(issubclass(Addition,Calculator))
# print(issubclass(Subtract,Calculator))
# print(issubclass(Multiply,Calculator))