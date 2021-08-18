class Bird:
    def speak(self):
        print("bird is speaking")
class Crow(Bird):
    def kaoo(self):
        print("crow kaoos")
d=Crow()
d.kaoo()
d.speak()