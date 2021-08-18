fruits={"orange","apple","banana","grapes"}
juice={"banana","greenapple","pineapple"}
print(fruits)
print(juice)
fruits.add("mango")
print(fruits)
fruits.remove("apple")
print(fruits)
print(fruits.intersection(juice))
print(fruits.union(juice))
print(juice.issubset(fruits))
print(fruits.difference(juice))


