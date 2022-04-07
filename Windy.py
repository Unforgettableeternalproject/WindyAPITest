import requests
from bs4 import BeautifulSoup

f = open("output.txt", "w", encoding="utf-8")


data = {"lat": 22.464,
        "lon": 120.441,
        "model": "gfs",
        "parameters": ["wind"],
        "levels": ["surface", "1000h"],
        "key": "JdhDvmUgYdlabcxz9fzobkQDNGc4MbMz"
        }
header = {"Content-Type" :"application/json"}
s = requests.post("https://api.windy.com/api/point-forecast/v2", json = data, headers = header)

lst = s.text.split('"')
fs_ = ""
useless = 0
for i in lst:
    if(i == "warning"): break
    if(i == "wind_u-surface"): useless += 1
    if(useless == 2): fs_ = fs_ + i + "\n\n"
    
f.write("This is the start of the document.\n\n" + fs_ + "This is the end of the document.")

#f.write(str(s_) + "\nThis is the end of the document.")

