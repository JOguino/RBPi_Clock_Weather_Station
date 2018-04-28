import json
import urllib.request
import math
from IPLoc import IPLoc

# 'Gracefully' coded by Eren Yildirir.

class OWMInterface:
    def __init__(self, lat=33.78, lon=-84.40, unit='imperial'):
        appid = '96274c53ba08cc79a967497bbcadadc0'
        service = 'http://api.openweathermap.org/data/2.5/weather?'
        self.location = [lat, lon]
        self.url = urllib.request.Request('%slat=%d&lon=%d&units=%s&APPID=%s' %(service, lat, lon, unit, appid))
        self.data = []
        self.unitSet = unit
        self.call()

    def call(self):
        with urllib.request.urlopen(self.url) as response:
            jsonBatch = response.read()
        self.data = json.loads(jsonBatch.decode('utf-8'))

    def weatherMain(self):
        return str(self.data['weather'][0]['main'])

    def weatherDesc(self):
        return str(self.data['weather'][0]['description'])

    def temperature(self):
        return float(self.data['main']['temp'])

    def pressure(self):
        return float(self.data['main']['pressure'])

    def humidity(self):
        return float(self.data['main']['humidity'])

    def chanceOfRain(self):

        # Cloudiness effect on Rain Chance
        cloudFactor = ((float(self.data['clouds']['all'])/100) - 0.40) * 100/60
        if cloudFactor<0:
            cloudFactor = 0

        # Humidity effect on Rain Chance
        humidityFactor = float(self.data['main']['humidity'])/100

        # 'Dew Point vs Actual Temp' effect on Rain Chance
        temp = float(self.data['main']['temp'])
        tempmin = float(self.data['main']['temp_min'])
        if self.unitSet == 'imperial':
            temp = (temp-32)/1.8
            tempmin = (tempmin-32)/1.8
        elif self.unitSet == 'default':
            temp = temp -272.15
            tempmin = tempmin -272.15

        # Coeffs for Magnus' Equation
        beta = 17.62
        gamma = 243.12

        # Magnus' Equation for Dew Point
        dpNum = gamma*(math.log(humidityFactor) + (beta*temp)/(gamma+temp))
        dpDenom = beta - (math.log(humidityFactor) + (beta*temp)/(gamma+temp))
        dewPoint = dpNum/dpDenom
        tempFactor = 1-(tempmin-dewPoint/10)
        if tempFactor < 0:
            tempFactor = 0

        # Averaging with custom factors. Subject to change.
        chance = (math.pow(cloudFactor, 1) * math.pow(humidityFactor, 0.2) * math.pow(tempFactor, 0.6)) * 100
        return chance


##if __name__ == "__main__":
def getWeatherData():
    loc = IPLoc()
    coords = loc.getLoc()
    OWM = OWMInterface(lat=coords[0], lon=coords[1])
    OWM.call()
    print('Weather: %s (%s)' %(OWM.weatherMain(), OWM.weatherDesc()))
    print('Temperature: %d F' %(OWM.temperature()))
    print('Pressure: %d hPa' %(OWM.pressure()))
    print('Humidity: %d %%' %(OWM.humidity()))
    print('Rain chance: %d %%' %(OWM.chanceOfRain()))
    weatherdata = {'Weather Main': OWM.weatherMain(),
                   'Weather Description': OWM.weatherDesc(),
                   'Temperature': OWM.temperature(),
                   'Pressure': OWM.pressure(),
                   'Humidity': OWM.humidity(),
                   'Rain chance': OWM.chanceOfRain()
                   }
    return weatherdata
    
