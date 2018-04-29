#!/usr/bin/python3

import tkinter
import time
from sense_hat import SenseHat
import OWMInterface as OWM
import PixelArray as PA
import frames


sense = SenseHat()
sense.clear()
sensorData = {'humidity': sense.get_humidity(), 'temperature': sense.get_temperature(),'pressure': sense.get_pressure()}


class Clock(tkinter.Label):
        """ Class that contains the clock widget and clock refresh """

        def __init__(self, parent=None, seconds=True, colon=False):
                """
                Create and place the clock widget into the parent element
                It's an ordinary Label element with two additional features.
                """
                tkinter.Label.__init__(self, parent)

                self.display_seconds = seconds
                if self.display_seconds:
                        self.time     = time.strftime('%H:%M:%S')
                else:
                        self.time     = time.strftime('%I:%M %p').lstrip('0')
                self.display_time = self.time
                self.configure(text=self.display_time)
                self.after(200, self.tick)


        def tick(self):
                """ Updates the display clock every 200 milliseconds """
                if self.display_seconds:
                        new_time = time.strftime('%H:%M:%S')
                else:
                        new_time = time.strftime('%I:%M %p').lstrip('0')
                if new_time != self.time:
                        self.time = new_time
                        self.display_time = self.time
                        self.config(text=self.display_time)
                self.after(200, self.tick)
                

class Room_Temperature_Frame(tkinter.Label):
    sensorData['temperature'] = sense.get_temperature()
    def __init__(self,parent):
        tkinter.Frame.__init__(self, parent, width=333, height =50)
        self.Label = tkinter.Label(self, text= str('%0.d' %(sensorData['temperature'])) + " °C",
                                               fg='white',
                                               bg='#292b5d',
                                               font=("alfie",72)).pack()
        self.update()
        
    def update(self):
        sensorData['temperature'] = sense.get_temperature()
        self.Label.configure(text= str('%0.d' %(sensorData['temperature'])) + " °C",
                                               fg='white',
                                               bg='#292b5d',
                                               font=("alfie",72))
        self.after(1000, self.update)


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
        clock1 = Clock(clock_frame)
        clock1.pack()
        clock1.configure(bg='#292b5d',fg='silver',font=("alfie",200))
        bottom_blank_label = tkinter.Label(clock_frame, text=" ").pack()

        

 #       tkinter.Label(clock_frame, text="Have a nice day.",fg='white',bg='#292b5d').pack()
        
       
##       outside temperature 
        outside_temperature = tkinter.Frame(width=333, height=50)
        outside_temperature_label = tkinter.Label(outside_temperature, text="19 °C", fg='white',bg='#292b5d',font=("alfie",72)).pack()
        outside_temperature.place(in_=mainframe, anchor="c", relx=1/6.0, rely=.2)
        
        
##        outside_pressure
        outside_pressure = frames.Outside_Pressure(window)
        outside_pressure.place(in_=mainframe, anchor="c", relx=3/6.0, rely=.2)
        
##        outside humidity
        outside_humidity = tkinter.Frame(width=333, height=50)
        outside_humidity.place(in_=mainframe, anchor="c", relx=5/6.0, rely=.2)
        outside_humidity_label = tkinter.Label(outside_humidity, text="100%", fg='white',bg='#292b5d',font=("alfie",72)).pack()

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


        window.mainloop()
        

