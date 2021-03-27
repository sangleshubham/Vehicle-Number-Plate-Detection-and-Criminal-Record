import requests
from bs4 import BeautifulSoup
import re
imgpath = "data/img/30.jpg"

location = ""

proxies = {"http": "http://160.119.54.12:8080", "https": "http://160.119.54.12:8080"}
headers = {'Referer': 'https://google.com/index'}
with open(imgpath , 'rb') as f:
    location = requests.post("https://app.platerecognizer.com/alpr-demo" , files={"upload":f} , proxies=proxies , verify=False , allow_redirects=False, headers=headers).headers['Location'] 

data = requests.get("https://app.platerecognizer.com" + location , proxies=proxies , verify=False ).content

# print(data)

regex = "[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{4}"

print(re.findall(regex , str(data)))
