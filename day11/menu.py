import collections
import re
print("Select an option from menu")
print("\n")
print("1. AddEmployee")
print("2. Viewemployee")
choice=int(input("enter the choice"))
li=[]
if(choice==1):
    for i in range(2):
        dict={}
        print("AddEmployee is selected")
        dict["name"]=input("enter the empname:")
        dict["id"]=input("enter the emp id:")
        dict["designation"]=input("enter the designation:")
        salary=input("enter the salary:")
        amount=re.search("^[0-9]",salary)
        if amount:
            dict['salary']=salary
        dict["address"]=input("enter the address:")
        # dict["phone"]=input("enter the phone no:")
        phn =input("enter the phone no:")
        validation=re.search("^[6-9]\d{9}$",phn)
        if validation:
            dict["phone"]=phn
        pincode=input("enter the pincode:")
        validation1=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
        if validation1:
            dict['pincode']=pincode
        li.append(dict)
    c=int(input("2. ViewEmp - "))
    if(c==2):
        print("ViewEmp is selected")
        for i in range(len(li)-1):
            comb_dict=collections.ChainMap(li[i],li[i+1])
            print(comb_dict)
else:
    print("wrong option selected")
