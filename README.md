# RBPi_Clock_Weather_Station
## BY Joshua Owens, Nazli Goller, Eren Yildirir

# Bedside Weather Station

The Bedside Weather Station project displays the weather information such as temperature, humidity, pressure and successive weather display of the day.

This is a complete Raspberry Pi weather system with just the base Raspberry Pi hardware and the Raspberry Pi Sensehat.
You can find the video of the project below:

https://youtu.be/yVVe4LodSj8

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

 #### Software Used
 
  * latest version of Rapsberry Pi OS
  * Python 3
  * Tkinter (usually comes with python3)
 
# Getting Started
Boot Raspbian Image (as of writing this, Raspbian Stretch April 18, 2018)

Set up wifi.

Run following terminal commands.
```
How to run via terminal

### Installing
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/JOguino/RBPi__Clock_Weather_Station

python3 main.py
```
# How it was made

## GUI
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

Ambient light was implemented using the built in sensehat LEDS to give a RGB effect telling the user what the weather condition outside is.  

<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5919.jpg" width="400"/>
</p>

## Time:
The clock will grab the time from the system and update every second.  
An NTP method has been written that can grab the time and date. 

## Sensor Data:  
Sensor data is polled every second and updated.
If the raspberry pi has been running a while, the temperature sensor on the Sense hat will run higher because of the ambient heat coming from the processor. Therefore a manual correction was added to the code to account for this. The correction can be found in  
Frames.py -> Room_Temprature -> udate()  
Arduino code has been written and implemented that can read sensor data furhter away from the raspberry pi.  
Serial communication will be used to transmit the data.

## Weather Data  
Using OpenWeatherMap, data was grabbed posted in the GUI.  
OWMInterface gives details to how the data is grabbed and what functions are used.

## What's Next? How to improve.
### External Sensors
#### Temperature/Humidity/Pressure Sensor 
Because the temperatures are so close to the processor, they heat up causing inaccurate results.
Arduino code has been uploaded that uses exteral processor (an Arduino Uno in this case), to allow for the sesnsors to be further away from non-environmental affecting elements.  
The sensor data will be sent from the Arduino to the Raspberry Pi
#### Real time clock  
Internet will not always be avaialbe, therefore having a Real Time Clock module will be nice to keep time incase the NTP protocol cant be implemented. 

#### Hardware Used for Arduino version
 * Raspberry Pi 3 B+ (comes with the following)
     * Wifi module
 * Arduino Uno
 * Adafruit HTU21D-F (humidity and temperature sensor)
 * Sparkfun MPL3115A2 (Altitude/Pressure Sensor)
 * Tiny RTC I2C Module (real time clock module)
 * Sense Hat (comes with the following)
    * RGB LEDs
 * Adafruit A800 screen (1280x800 HDMI screen)

### Add Date  
NTPTimeSync.py grabs the date. Modify the strings inside the Clock.py Class to allow for date to be displayed

### Add Symbol for Weather Condition
using PIL (Pillow) for python3 we are able to put images into the GUI, 
main_off_board_mac.py (was used for prototyping with macs away from raspberry pi)
implements this feature to add a symbol for weather condition


## OWMInterface Class
OWMInterface is a class built to query the web API (OpenWeatherMap in this case) for the outside weather, and decode the response into information accessible by method calls. It requires some modification to run it on a presonalised system, since OpenWeatherMap requires users to get an APPID (available for free) to access their services. This personal APPID must be set inside the class "init" to be able to get correct responses to the web queries.

### "init"
Runs at the initialisation of the class object. This is where the APPID needs to be set, and where the class parameters such as service address, location and unit variables are created. This class also automatically calls the "call()" to query the web API to get initial response.

| Input | Description |
| ----------  | :----- |
| `lat`  | The Lattidute from IPLoc or other positioning system. |
| `lon`  | The Longitude from IPLoc or other positioning system. |
| `unit` | The desired unit system the response should be in. "metric", "imperial"(default) or "default"(as in Web API default returns in Kelvins) |

| Output | Description |
| ----- | ---- |
| _None_ | (Used to create the class object.) |

### "call()"
Queries the web API for weather data, and decodes the received JSON into the list "data".

| Input | Description |
| ----------  | :----- |
| _None_ | (No inputs) |

| Output | Description |
| ----- | :---- |
| _None_ | (Used to update in-object parameters.) |

### "weatherMain()"
Returns the general weather classification ("Clear", "Cloudy", "Rain" etc.)

| Input | Description |
| ----  | :---- |
| _None_ | (No inputs) |

| Output | Description |
| ---- | :---- |
| _string_ | The general weather classification. |

### "weatherDesc()"
Returns the specific weather description (such as "Scattered Clouds")

        weather_stuff = [("clear sky", "01d.png"),
                          ("few clouds", "02d.png"),
                          ("scattered clouds", "03d.png"),
                          ("broken clouds", "04d.png"),
                          ("shower rain", "09d.png"),
                          ("rain", "10d.png"),
                          ("thunderstorm", "11d.png"),
                          ("snow", "13d.png"),
                          ("mist", "50d.png")]
        
        current_weather = 0 # TODO: This is where we choose the correct weather index from above ^
        iconset = "icons"  # can do alternative_icons too
        
        weather = tkinter.Frame(width=200, height=50)
        weather.place(in_=mainframe, anchor="w", relx=leftcol, rely=.1)
        weather_label = tkinter.Label(weather , text= weather_stuff[current_weather][0].capitalize(), fg='white',bg='#292b5d',font=("alfie",60)).pack()

| Output | Description |
| ---- | :---- |
| _string_ | The specific weather description. |

### "weatherIcon()"
Returns the weather icon code to load the specific icon for the weather condition (such as "01d")

weather_stuff = [("clear sky", "01d.png"),
                          ("few clouds", "02d.png"),
                          ("scattered clouds", "03d.png"),
                          ("broken clouds", "04d.png"),
                          ("shower rain", "09d.png"),
                          ("rain", "10d.png"),
                          ("thunderstorm", "11d.png"),
                          ("snow", "13d.png"),
                          ("mist", "50d.png")]
        
        current_weather = 0 # TODO: This is where we choose the correct weather index from above ^
        iconset = "icons"  # can do alternative_icons too
        
        weather = tkinter.Frame(width=200, height=50)
        weather.place(in_=mainframe, anchor="w", relx=leftcol, rely=.1)
        weather_label = tkinter.Label(weather , text= weather_stuff[current_weather][0].capitalize(), fg='white',bg='#292b5d',font=("alfie",60)).pack()
        
        load = Image.open(os.path.join(iconset, weather_stuff[current_weather][1]))
        render = ImageTk.PhotoImage(load)
        
        weather_logo = tkinter.Frame(width=200, height=50, background="#292b5d")
        weather_logo.place(in_=mainframe, anchor="c", relx=midcol, rely=.1)
        weather_logo_label = tkinter.Label(weather_logo, background="#292b5d", image=render,font=("alfie",60)).pack()

| Output | Description |
| ---- | :---- |
| _string_ | The specific weather icon code. |

### "temperature()"
Returns the temperature at the time of the query, in the units set in the object initialisaion.

        room_temperature = frames.Room_Temperature(window)
        room_temperature.place(in_=mainframe, anchor="w", relx=leftcol, rely=.8)

        outside_temperature = frames.Outside_Temperature(window)
        outside_temperature.place(in_=mainframe, anchor="w", relx=leftcol, rely=.2)

| Output | Description |
| ---- | :---- |
| _float_ | The temperature value. |

### "pressure()"
Returns the atmospheric pressure at the time of the query, in _hPa_.

        room_pressure = frames.Room_Pressure(window)
        room_pressure.place(in_=mainframe, anchor="c", relx=midcol, rely=.8)

        outside_pressure = frames.Outside_Pressure(window)
        outside_pressure.place(in_=mainframe, anchor="c", relx=midcol, rely=.2)

| Output | Description |
| ---- | :---- |
| _float_ | The atmospheric pressure value. |

### "Humidity()"
Returns the relative humidity percentage at the time of the query.

        room_humidity = frames.Room_Humidity(window)
        room_humidity.place(in_=mainframe, anchor="e", relx=rightcol, rely=.8)
        
        outside_humidity = frames.Outside_Humidity(window)
        outside_humidity.place(in_=mainframe, anchor="e", relx=rightcol, rely=.2)

| Output | Description |
| ---- | :---- |
| _float_ | The humidity percentage. |

### "chanceOfRain()"
Uses the "cloudiness", relative humidity, and the difference between the outside temperature and the dew point to give a crude prediction on the chance of rain.
To calculate the dew point, it uses Magnus' equation with relative humidity and the temperature.

_The averaging parameters and the cutoffs for these factors are tuned by trial and error, and are open to change for improvement._
 
        chance_rain = tkinter.Frame(width=200, height=50)
        chance_rain.place(in_=mainframe, anchor="e", relx=rightcol, rely=.1)
        chance_rain_label = tkinter.Label(chance_rain , text="30%", fg='white',bg='#292b5d',font=("alfie",60)).pack()

| Output | Description |
| ---- | :---- |
| _float_ | The percent change of rain. |

### "gerWeatherData()"
Returns a list of weather parameters (weatherMain, weatherDesc weatherIcon, temperature, pressure, humidiry, chanceOfRain at the time of the query.
#### Input

| Input | Description |
| ----  | :---- |
| _None_ | (No inputs) |

| Output | Description |
| ---- | :---- |
| _List_ | All weather condition parameters compiled together in a list.

## IPLoc Class
IPLoc queries an IP geolocation service to provide the lattitude and the longitude required for the weather data.

### "init"
Runs at the initialisation of the class object. This is where the class parameters such as service address and data variables are created. This class also automatically calls the "call()" to query the web service to get initial response.  

| Input | Description |
| ----  | :---- |
| _None_ | (No inputs) |

| Output | Description |
| ----- | ---- |
| _None_ | (Used to create the class object.) |

### "call()"
Queries the web service for IP info, and decodes the received JSON into the list "data".

| Input | Description |
| ----------  | :----- |
| _None_ | (No inputs) |

| Output | Description |
| ----- | :----- |
| _None_ | (Used to update in-object parameters.) |

### "getLoc()"
Returns the lattitude and longitude.

| Input | Description |
| ----  | :---- |
| _None_ | (No inputs) |

| Output | Description |
| ---- | :---- |
| _float[]_ | The lattitude and longitude in float, in an array. |

### "getCity()"
Returns the city for the location.

| Input | Description |
| ----  | :---- |
| _None_ | (No inputs) |

| Output | Description |
| ---- | :---- |
| _string_ | The city name. |

### "getRegion()"
Returns the region/state for the location.

| Input | Description |
| ----  | :---- |
| _None_ | (No inputs) |

| Output | Description |
| ---- | :---- |
| _string_ | The region/state name. |

### "getZipcode()"
Returns the zip code for the location.

| Input | Description |
| ----  | :---- |
| _None_ | (No inputs) |

| Output | Description |
| ---- | :---- |
| _string_ | The zipcode. |



```
Give examples

Install latest version of Raspberry Pi OS.

### Installing

sudo apt-get install python3

```



## Images
<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5915.jpg" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5919.jpg" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5920.jpg" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5917.jpg" width="400"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5922.jpg" width="400"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5932.JPG" width="400"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5937.JPG" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5945.JPG" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5943.JPG" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5944.JPG" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5934.JPG" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5939.JPG" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5942.JPG" width="400"/>
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5941.JPG" width="400"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/IMG_5938.JPG" width="400"/>
</p>
