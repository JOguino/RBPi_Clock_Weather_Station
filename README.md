# RBPi_Clock_Weather_Station

# Bedside Weather Station

Internal (Sensor)/ External (API) temperature, pressure, humidity, real clock time.

The Bedside Weather Station project displays the weather information such as temperature, humidity, pressure and successive weather display of the day.

This is a complete Raspberry Pi weather system with just the base Raspberry Pi hardware and the Raspberry Pi Sensehat.

Python code was implemented that read the sensor values. 
Tkinter was used to create a window that would display the time.
<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/20180501_102106.jpg" width="200"/>
</p>

The format is as followed:
```
weather condition               percent chance of rain
Outside Temp     Outside Pressure       Outside Humidity
----------------------------------------------------------
Hours:Minutes:Seconds
----------------------------------------------------------
Inside Temp      Inside Pressure        Inside Humidity
```


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Raspberry Pi 3 
* Breadboard wire bundle
* Breadboard
* Pressure Sensor
* Humidity Sensor
* Temperature Sensor
* RGB LEDs
* Wifi module
* Real time clock module
* Display

### Hardware Used for Sensehat version
  * Raspberry Pi 3 B+ (comes with the following)
      * Wifi module
        * NTP Protocol was used instead of Real Time Clock Module
  * Sense Hat (comes with the following)
      * Pressure Sensor
      * Humidity Sensor
      * Temperature Sensor
      * RGB LEDs
  * Adafruit A800 screen (1280x800 HDMI screen)

 #### What things you need to install the software and how to install them

  * latest version of Rapsberry Pi OS
  * Python 3
  * Tkinter (usually comes with python3)
  

### Hardware Used for Arduino version
 * Raspberry Pi 3 B+ (comes with the following)
     * Wifi module
 * Arduino Uno
 * Adafruit HTU21D-F (humidity and temperature sensor)
 * Sparkfun MPL3115A2 (Altitude/Pressure Sensor)
 * Tiny RTC I2C Module (real time clock module)
 * Sense Hat (comes with the following)
    * RGB LEDs
 * Adafruit A800 screen (1280x800 HDMI screen)
 
 
 




```
Give examples

Install latest version of Raspberry Pi OS.

### Installing

sudo apt-get install python3

```

## OWMInterface Class
OWMInterface is a class built to query the web API (OpenWeatherMap in this case) for the outside weather, and decode the response into information accessible by method calls. It requires some modification to run it on a presonalised system, since OpenWeatherMap requires users to get an APPID (available for free) to access their services. This personal APPID must be set inside the class "init" to be able to get correct responses to the web queries.

### "init"
Runs at the initialisation of the class object. This is where the APPID needs to be set, and where the class parameters such as service address, location and unit variables are created. This class also automatically calls the "call()" to query the web API to get initial response.  
#### Input
__lat:__ The Lattidute from IPLoc or other positioning system.

__lon:__ The Longitude from IPLoc or other positioning system.

__unit:__ The desired unit system the response should be in. "metric", "imperial"(default) or "default"(as in Web API default returns in Kelvins)
#### Output
Used to create the class object.

### "call()"
Queries the web API for weather data, and decodes the received JSON into the list "data".
#### Input
_NONE_
#### Output
_NONE_
Used to update in-object parameters.

### "weatherMain()"
Returns the general weather classification ("Clear", "Cloudy", "Rain" etc.)
#### Input
_NONE_
#### Output
A string with the general weather classification.

### "weatherDesc()"
Returns the specific weather description (such as "Scattered Clouds")
#### Input
_NONE_
#### Output
A string with the specific weather description.

### "weatherIcon()"
Returns the weather icon code to load the specific icon for the weather condition (such as "01d")
#### Input
_NONE_
#### Output
A string with the specific weather icon code.

### "temperature()"
Returns the temperature at the time of the query, in the units set in the object initialisaion.
#### Input
_NONE_
#### Output
A float with the temperature value.

### "pressure()"
Returns the atmospheric pressure at the time of the query, in _hPa_.
#### Input
_NONE_
#### Output
A float with the atmospheric pressure value.

### "Humidity()"
Returns the relative humidity percentage at the time of the query.
#### Input
_NONE_
#### Output
A float with the temperature value.

### "chanceOfRain()"
Uses the "cloudiness", relative humidity, and the difference between the outside temperature and the dew point to give a crude prediction on the chance of rain.
To calculate the dew point, it uses Magnus' equation with relative humidity and the temperature.

_The averaging parameters and the cutoffs for these factors are tuned by trial and error, and are open to change for improvement._
#### Input
_NONE_
#### Output
A float with percent chance of rain.

### "gerWeatherData()"
Returns a list of weather parameters (weatherMain, weatherDesc weatherIcon, temperature, pressure, humidiry, chanceOfRain at the time of the query.
#### Input
_NONE_
#### Output
A list with all the weather condition parameters.

## IPLoc Class
IPLoc queries an IP geolocation service to provide the lattitude and the longitude required for the weather data.

### "init"
Runs at the initialisation of the class object. This is where the class parameters such as service address and data variables are created. This class also automatically calls the "call()" to query the web service to get initial response.  
#### Input
_NONE_
#### Output
Used to create the class object.

### "call()"
Queries the web service for IP info, and decodes the received JSON into the list "data".
#### Input
_NONE_
#### Output
_NONE_
Used to update in-object parameters.

### "getLoc()"
Returns the lattitude and longitude.
#### Input
_NONE_
#### Output
A list with lattitude and longitude in float.

### "getCity()"
Returns the city for the location.
#### Input
_NONE_
#### Output
A string with the city name.

### "getRegion()"
Returns the region/state for the location.
#### Input
_NONE_
#### Output
A string with the region/state name.

### "getZipcode()"
Returns the zip code for the location.
#### Input
_NONE_
#### Output
A string with the zipcode.


## Images
<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/20180501_102106.jpg" width="50"/>
</p>
