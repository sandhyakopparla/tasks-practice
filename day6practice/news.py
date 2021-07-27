import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4ead903828934b658503878636459c1b")
print(data.text)