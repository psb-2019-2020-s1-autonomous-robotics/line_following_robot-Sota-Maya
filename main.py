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
moving_motor = Motor(Port.A)
rotating_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)

while Button.LEFT not in brick.buttons():
    wait(1)
white = color_sensor.reflection()
brick.sound.beep()
while Button.RIGHT not in brick.buttons():
    wait(1)
black = color_sensor.reflection()
brick.sound.beep()
deciding_value = (white + black)/2
while True:
    if color_sensor.reflection() < deciding_value: #Checks to see if the robot is on line
        brick.display.text("%s Sensed line" % color_sensor.reflection())
        moving_motor.reset_angle(0)
        moving_motor.run_target(500, -90) #Moves robot forward
    else: 
        brick.display.text("%s Nothing sensed, searching." % color_sensor.reflection())
        incrament = 2
        a = incrament
        b = 1
        while color_sensor.reflection() > deciding_value:
            rotating_motor.run_target(500,a*b)
            a = a + incrament
            b = - b
