import json
import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4ead903828934b658503878636459c1b")
ExtractedData=data.json()
articles=ExtractedData["articles"]
vowel="aeiou"
for i in articles:
    title=i["title"]
    count={}.fromkeys(vowel,0)
    print(title)
    for x in title.lower():
        if x in count:
            count[x]=count[x]+1
    print(count)