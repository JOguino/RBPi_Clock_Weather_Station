
#include <Wire.h>
#include "RTClib.h"
#include "Adafruit_HTU21DF.h"
#include "SparkFunMPL3115A2.h"

RTC_DS1307 RTC;
MPL3115A2 myPressure;
Adafruit_HTU21DF htu = Adafruit_HTU21DF();

void setup () {
    Serial.begin(9600);
    Wire.begin();
    RTC.begin();
    RTC.adjust(DateTime(__DATE__, __TIME__));
  if (! RTC.isrunning()) {
    Serial.println("RTC is NOT running!");
    // following line sets the RTC to the date & time this sketch was compiled
    RTC.adjust(DateTime(__DATE__, __TIME__));
  }
  myPressure.begin(); // Get sensor online

  // Configure the sensor
  //myPressure.setModeAltimeter(); // Measure altitude above sea level in meters
  myPressure.setModeBarometer(); // Measure pressure in Pascals from 20 to 110 kPa
  
  myPressure.setOversampleRate(7); // Set Oversample to the recommended 128
  myPressure.enableEventFlags(); // Enable all three pressure and temp event flags 
  if (!htu.begin()) {
    Serial.println("Couldn't find sensor!");
    while (1);
  }
}
void loop () {
    DateTime now = RTC.now(); 
    Serial.print(now.year(), DEC);
    Serial.print('/');
    Serial.print(now.month(), DEC);
    Serial.print('/');
    Serial.print(now.day(), DEC);
    Serial.print(' ');
    Serial.print(now.hour(), DEC);
    Serial.print(':');
    Serial.print(now.minute(), DEC);
    Serial.print(':');
    Serial.print(now.second(), DEC);
    Serial.print("  "); 
    Serial.print("  Temp= "); Serial.print(htu.readTemperature());
    Serial.print("  Hum= "); Serial.print(htu.readHumidity());
    float pressure = myPressure.readPressure();
    Serial.print("  Pres= "); Serial.print(pressure, 2);
  
    Serial.println();
    delay(1000);
}
