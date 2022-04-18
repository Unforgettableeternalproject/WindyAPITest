from requests import get

class electricity:
    def __init__(self):
        pass
    
    def fetch(self):
        self.site = get('https://www.taipower.com.tw/d006/loadGraph/loadGraph/data/genary.json')
        self.datas = self.site.text.split(',')

        self.useless = 0
        self.get = []
        for i in self.datas:
            if(i == '"台中港"'): self.useless = 1
            if(self.useless == 1 and i == '" "]'): break
            if(self.useless == 1):self.get.append(i)
        self.get.pop(0)
        self.get.pop(0)
        
        self.pgpre = self.get[0].split('"')
        self.pg = self.pgpre[1]
        
        self.pgppre = self.get[1].split('"')
        self.pgp = self.pgppre[1]
        
        return self.pg + "MW", self.pgp
    
