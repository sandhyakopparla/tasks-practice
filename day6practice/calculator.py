class Calculator:
    def add(self,a1,a2):
        return a1+a2
    def sub(self,a1,a2):
        return a1-a2
    def mul(self,a1,a2):
        return a1*a2
    def div(self,a1,a2):
        return a1/a2
    def floor(self,a1,a2):
        return a1//a2
calculate=Calculator()
a1=int(input("enter the value:"))
a2=int(input("enter the value:"))
print(calculate.add(a1,a2))
print(calculate.sub(a1,a2))
print(calculate.mul(a1,a2))
print(calculate.div(a1,a2))
print(calculate.floor(a1,a2))