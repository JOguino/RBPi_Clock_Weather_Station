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

Time:
The clock will grab the time from the system and update every second. An NTP method has been written that can grab the time and date. It just has to be displayed.

Sensor Data:
Sensor data is polled every second and updated depending on the readings.
If the raspberry pi has been running a while, the temperature sensor on the Sense hat will run higher because of the ambient heat coming from the processor.
Arduino code has been written and implemented that can read sensor data furhter away from the raspberry pi.
Serial communication will be used to transmit the data.


## Getting Started

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



## Images
<p align="center">
  <img src="https://raw.githubusercontent.com/JOguino/RBPi_Clock_Weather_Station/master/images/20180501_102106.jpg" width="50"/>
</p>
