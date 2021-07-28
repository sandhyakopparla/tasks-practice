import json
import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4ead903828934b658503878636459c1b")
ExtractedData=data.json()
articles=ExtractedData["articles"]
print(len(articles))
for i in articles:
    print(i["title"])
