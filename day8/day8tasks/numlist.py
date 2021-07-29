# list=[1,2,3,4,5]
# new=[i for i in list if i%2==0 ]
# print(new)
list=["malayalam","english","sandhya","mom"]
new=[i for i in list if i==i[::-1]]
print(new)
