import requests

url = "https://www.shutterstock.com/_next/data/5672de8ee3a/en/search/cat.json?term=cat"
extra = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"}
response = requests.get(url, headers= extra)

print(response.json())