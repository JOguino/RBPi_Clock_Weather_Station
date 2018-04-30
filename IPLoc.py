import json
import urllib.request
import time
# 'Gracefully' coded by Eren Yildirir.

class IPLoc:
    def __init__(self):
        self.url = urllib.request.Request('https://ipinfo.io/json')
        self.data = []
        self.call()

    def call(self):
        called = False
        while not called:
            try:
                with urllib.request.urlopen(self.url) as response:
                    jsonBatch = response.read()
                self.data = json.loads(jsonBatch.decode('utf-8'))
                called =True
            except:
                print('Retry Network')
                time.sleep(1)
        

    def getLoc(self):
        strLoc = self.data['loc']
        coords = strLoc.split(',')
        return [float(coords[0]), float(coords[1])]

    def getCity(self):
        return self.data['city']

    def getRegion(self):
        return self.data['region']

    def getZipcode(self):
        return self.data['postal']


if __name__ == '__main__':
    loc = IPLoc()
##    print(loc.getLoc())
##    print(loc.getCity())
##    print(loc.getRegion())
##    print(loc.getZipcode())


