# RBPi_Clock_Weather_Station

# Bedside Weather Station

Internal (Sensor)/ External (API) temperature, pressure, humidity, real clock time.

The Bedside Weather Station project displays the weather information such as temperature, humidity, pressure and successive weather display of the day.

This is a complete Raspberry Pi weather system with just the base Raspberry Pi hardware, and some assorted analog and digital sensors to make our measurements. No buying pre-made anemometers or rain gauges — we are making our own!

Each of those sensors uses different type of python or even C code to get the readings. Both of them store the results in the database in pretty much the same way. Generally speaking, the code works as follows. In the first run, it creates a new table and with setting up a ?, this process is repeated every ? minutes. This way we get a nice overview of the temperatures during the day.

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

### Hardware Used
  * Raspberry Pi 3 B+ (comes with the following)
      * Wifi module
        * NTP Protocol was used instead of Real Time Clock Module
  * Sense Hat (comes with the following)
      * Pressure Sensor
      * Humidity Sensor
      * Temperature Sensor
      * RGB LEDs
  * Adafruit A800 screen (1280x800 screen)
    

What things you need to install the software and how to install them

  * latest version of Rapsberry Pi OS
  * Python 3
  * Tkinter (usually comes with python3)
  


```
Give examples

Install latest version of Raspberry Pi OS.

### Installing

sudo apt-get install python3

```



## Images
<p align="center">
  <img src="https://github.com/JOguino/RBPi_Clock_Weather_Station/blob/master/icons/01d.png?raw=true" width="350"/>
  <img src="https://github.com/JOguino/RBPi_Clock_Weather_Station/blob/master/icons/01d.png?raw=true" width="350"/>
</p>
