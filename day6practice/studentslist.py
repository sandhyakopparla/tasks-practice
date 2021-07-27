class Students:
    def __init__(self,name,rollno,adminno):
        self.myname=name
        self.myrollno=rollno
        self.myadminno=adminno
obj=[]
obj.append(Students("rahul",101,3445))
obj.append(Students("sandhya",102,3446))
obj.append(Students("arun",104,3449))
print(obj[0].myname)
print(obj[1].myname)
print(obj[1].myrollno)
