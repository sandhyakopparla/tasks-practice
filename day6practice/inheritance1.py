class Animal:
    def speak(self,speak):
        self.speak=speak
        print(self.speak)
class Dog(Animal):
    def bark(self,bark):
        self.bark=bark
        print(self.bark)
objAnimal=Animal()
objDog=Dog()
objDog.speak("animal speaking")
objDog.bark("dog barking")

