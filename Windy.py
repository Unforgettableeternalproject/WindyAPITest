import requests

f = open("output.txt", "w", encoding="utf-8")


data = {"lat": 22.464,
        "lon": 120.441,
        "model": "gfs",
        "parameters": ["wind"],
        "levels": ["surface", "150h"],
        "key": "JdhDvmUgYdlabcxz9fzobkQDNGc4MbMz"
        }
header = {"Content-Type" :"application/json"}
s = requests.post("https://api.windy.com/api/point-forecast/v2", json = data, headers = header)

f.write(s.text)

