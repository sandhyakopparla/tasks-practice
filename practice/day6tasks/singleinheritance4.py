class Mobile:
    def mydisplay(self,display):
        self.display=display
        print(self.display)

class Brand(Mobile):
    def apple(self,ios):
        self.ios=ios
        print(self.ios)

obj=Brand()
obj.mydisplay("HD")
obj.apple("11.0")