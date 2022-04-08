import requests, math


class wind:
    def __init__(self):
        pass
    
    def fetch(self):
        self.data = {"lat": 23.38,
                    "lon": 120.08,
                    "model": "gfs",
                    "parameters": ["wind"],
                    "levels": ["950h"],
                    "key": "JdhDvmUgYdlabcxz9fzobkQDNGc4MbMz"
                    }
        self.header = {"Content-Type" :"application/json"}
        self.s = requests.post("https://api.windy.com/api/point-forecast/v2", json = self.data, headers = self.header)
        return self.s.text

    def optimize(self, s):
        self.lst = s.split('"')
        self.fs_ = ""
        self.lfs_ = []

        self.useless = 0
        for i in self.lst:
            if(i == "warning"): break
            if(i == "wind_u-950h"): self.useless += 1
            if(self.useless == 2): 
                self.lfs_.append(i)
                self.fs_ = self.fs_ + i + "\n\n"
        

        self.wu = self.lfs_[1].split(',')
        self.wv = self.lfs_[3].split(',')

        self.wu.pop()
        self.wv.pop()

        self.st = self.wu[0]
        self.nwu = float(self.st[2:])

        self.st = self.wv[0]
        self.nwv = float(self.st[2:])
        return self.nwu, self.nwv

    def calculate(self, nwu, nwv):
        self.dir = ''
        self.fws = 0
        if(nwu > 0 and nwv > 0): self.dir = "SouthWest"
        if(nwu > 0 and nwv < 0): self.dir = "NorthWest"
        if(nwu < 0 and nwv > 0): self.dir = "SouthEast"
        if(nwu < 0 and nwv < 0): self.dir = "NorthEast"
        if(nwu > 0 and nwv == 0): self.dir = "West"
        if(nwu < 0 and nwv == 0): self.dir = "East"
        if(nwu == 0 and nwv > 0): self.dir = "South"
        if(nwu == 0 and nwv < 0): self.dir = "North"

        self.fws = round(math.sqrt(nwu**2+nwv**2), 2)
        return str(self.fws) + "m/s", self.dir


