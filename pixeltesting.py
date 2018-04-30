#!/usr/bin/python3
from sense_hat import SenseHat
import PixelArray as PA

sense = SenseHat()
sense.set_pixels(PA.setPixelArray('13d'))