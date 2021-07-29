import json
import requests
data=requests.get("https://jsonplaceholder.typicode.com/posts")
Extracteddata=data.json()
#print(list(Extracteddata))
list=[]
for i in Extracteddata:
    list.append(i["title"])
lis=[x for x in list if x[0]=='a' in x]
print(lis)    

