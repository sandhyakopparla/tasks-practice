n1=int(input("enter the value:"))
even=[]
odd=[]
def evenorodd(n1):
    if(n1%2==0):
        even.append(n1)
    else:
        odd.append(n1)
    return n1
print(evenorodd(n1))
print(even)
print(odd)
