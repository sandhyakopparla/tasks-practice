class Cars:
    def minecolor(self,color):
        self.color=color
        print(self.color)
class BMW(Cars):
    def topSpeed(self,speed):
        self.speed=speed
        print(self.speed)
objcars=Cars()
objBMW=BMW()
objBMW.minecolor("white")
objBMW.topSpeed(150)