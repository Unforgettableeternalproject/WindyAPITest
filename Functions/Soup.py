import requests

f = open("output.txt", 'w', encoding= "utf-8")

site = requests.get('https://www.taipower.com.tw/d006/loadGraph/loadGraph/data/genary.json')

f.write(site.text)
f.close()