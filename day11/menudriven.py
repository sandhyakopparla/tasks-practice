import collections
import re
print("Select an option from menu")
print("\n")
print("1.Add students detials:")
print("2.search the students with roll no")
print("3.list the student api with marks")
print("4.print all the students")
choice=int(input("enter the choice"))
li=[]
if(choice==1):
    for i in range(3):
        dict={}
        print("add students details is selected")
        dict["name"]=input("enter the studentname:")
        dict["rollno"]=input("enter the roll no:")
        dict["admission no"]=input("enter the admission no:")
class Student():
    def marks(self,m1,m2,m3,m4,m5):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def print(self):
        print("enter the mark:",self.m1)
        print("enter the mark:",self.m2)
        print("enter the mark:",self.m3)
        print("enter the mark:",self.m4)
        print("enter the mark:",self.m5)
    li.append(dict)
if(choice==2):
    print("Search the students with roll no is selected")
def search(self,rollno):
    for i in range(li.__len__()):
        if(li(i).rollno==5):
            return i
if(choice==3):
    print("list the students api with marks")
    for i in range(len(li)-1):
            comb_dict=collections.ChainMap(li[i],li[i+1])
            print(comb_dict)
if(choice==4):
    print("print all the students selected")
    print(dict[students])
