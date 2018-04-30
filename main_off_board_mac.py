#!/usr/bin/python3

import tkinter
import time
#from sense_hat import SenseHat
import OWMInterface as OWM
import PixelArray as PA
import Frames as frames
import Clock as clock


if __name__ == "__main__":
        """
        Create a tkinter window and populate it with elements
        One of those elements merely happens to include the clocks.

        The clock widget can be configure()d like any other Label widget.
        Nothing special needs to be added to main(). The Clock class
            updates the widget automatically when you create the widget.

        """

        # Create window and frame
        window = tkinter.Tk()
        window.configure(background = 'white')
##        window.attributes('-fullscreen', True)
        mainframe = tkinter.Frame(width=800, height=600, background="#292b5d")
        mainframe.pack(fill="both", expand=True, padx=20, pady=20)

        clock_frame  = tkinter.Frame(window, width=800, height=600 )
        clock_frame.place(in_=mainframe, anchor="c", relx=.5, rely=.5)
        
        # Add the frame elements, including the clock like any other element
        #        top blank line
        #        time
        #        bottom blank line
        top_blank_label = tkinter.Label(clock_frame, text=" ").pack() 
        clock1 = clock.Clock(clock_frame)
        clock1.pack()
        clock1.configure(bg='#292b5d',fg='silver',font=("alfie",200))
        bottom_blank_label = tkinter.Label(clock_frame, text=" ").pack()

        

 #       tkinter.Label(clock_frame, text="Have a nice day.",fg='white',bg='#292b5d').pack()
        
       
##       outside temperature 
        outside_temperature = frames.Outside_Temperature(window)
        outside_temperature.place(in_=mainframe, anchor="c", relx=1/6.0, rely=.2)
        
        
##        outside_pressure
        outside_pressure = frames.Outside_Pressure(window)
        outside_pressure.place(in_=mainframe, anchor="c", relx=3/6.0, rely=.2)
        
##        outside humidity
        outside_humidity = frames.Outside_Humidity(window)
        outside_humidity.place(in_=mainframe, anchor="c", relx=5/6.0, rely=.2)

##        Create Room Values
##        room temperature
        room_temperature = frames.Room_Temperature(window)
        room_temperature.place(in_=mainframe, anchor="c", relx=1/6.0, rely=.8)

##        room pressure
        room_pressure = frames.Room_Pressure(window)
        room_pressure.place(in_=mainframe, anchor="c", relx=3/6.0, rely=.8)

##        room humidity
        room_humidity = frames.Room_Humidity(window)
        room_humidity.place(in_=mainframe, anchor="c", relx=5/6.0, rely=.8)
        
##   percent chance of rain  
        chance_rain = tkinter.Frame(width=200, height=50)
        chance_rain.place(in_=mainframe, anchor="e", relx=5.5/6.0, rely=.1)
        chance_rain_label = tkinter.Label(chance_rain , text="30%", fg='white',bg='#292b5d',font=("alfie",60)).pack()
        
##        weather condition
        weather_string = ["clear sky",
                          "few clouds",
                          "scattered clouds" ,
                          "broken clouds",
                          "shower rain",
                          "rain",
                          "thunderstorm",
                          "snow",
                          "mist"]
##        weather_string = "scattered clouds"
        weather = tkinter.Frame(width=200, height=50)
        weather.place(in_=mainframe, anchor="w", relx=.45/6.0, rely=.1)
        weather_label = tkinter.Label(weather , text= weather_string[2], fg='white',bg='#292b5d',font=("alfie",60)).pack()
        




        window.mainloop()
