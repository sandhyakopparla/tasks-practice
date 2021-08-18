class Animals:
    def eyes(self,eye):
        self.eye=eye
        print(eye)
    def foots(self,foot):
        self.foot=foot
        print(foot)
class Dog(Animals):
    def dogcolor(self,color):
        self.color=color
        print(color)
obj=Dog()
obj.eyes("blue")
obj.foots("black")
obj.dogcolor("white")