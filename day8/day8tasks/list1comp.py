# list=[i for i in range(2,4)]
# print(list)

# li=[i for i in range(2,500)]
# new=[j for j in li if j%2==1]
# print(new)

 


li =[]
for i in range(2,500):
    li.append(i)
print(li)
new = []
for j in li:
    if j%2==1:
        new.append(j)
print(new)