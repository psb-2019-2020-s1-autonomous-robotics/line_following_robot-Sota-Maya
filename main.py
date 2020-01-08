#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


brick.sound.beep()
#Sets up sensor and motors
moving_motor = Motor(Port.B)
rotating_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
print("Set up motors and sensor")
#Get the deciding value
while Button.LEFT not in brick.buttons():
    wait(1)
white = color_sensor.reflection()
brick.sound.beep()
while Button.RIGHT not in brick.buttons():
    wait(1)
black = color_sensor.reflection()
brick.sound.beep()
deciding_value = (white + black)/2
print("Deciding value = %s, white = %s. black = %s" % (deciding_value, white, black))
while True:
    if color_sensor.reflection() < deciding_value: #Checks to see if the robot is on line
        brick.display.text("%s Sensed line" % color_sensor.reflection())
        print("%s Sensed line" % color_sensor.reflection())
        moving_motor.reset_angle(0)
        print("reset angle")
        moving_motor.run_target(500, -90) #Moves robot forward
        print("moved forward")
    else: 
        brick.display.text("%s Nothing sensed, searching." % color_sensor.reflection())
        incrament = 2
        a = incrament
        b = 1
        while color_sensor.reflection() > deciding_value:
            rotating_motor.run_target(500,a*b)
            a = a + incrament
            b = - b
            print("searching")
        print("end of else")
    print("end of while")
