class Dress:
    def Fancy(self,jeans):
        self.jeans=jeans
        print(self.jeans)
class Modern(Dress):
    def Stylish(self,skirts):
        self.skirts=skirts
        print(self.skirts)
class Traditional(Modern):
    def orthodox(self,saree):
        self.saree=saree
        print(self.saree)
obj=Traditional()
obj.Fancy("jeans")
obj.Stylish("skirts")
obj.orthodox("saree")

