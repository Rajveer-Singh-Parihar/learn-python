import requests
import json
query = input(" what type of news you are  intesrested in ?")
url = f"https://newsapi.org/v2/everything?q={query}tesla&from=2023-12-05&sortBy=publishedAt&apiKey=API_KEY"
r = requests.get(url)
print(r.text)
news = json.koads(r.text)
for articles in news["articles"]:
    print(articles["title"])
    print(articles["description"])