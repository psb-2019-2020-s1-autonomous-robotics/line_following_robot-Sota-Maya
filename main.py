#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


brick.sound.beep()
front_motor = Motor(Port.A)
motorB = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)
deciding_value = 40
while True:
    if color_sensor.reflection() < deciding_value:
        motorB.reset_angle(0)
        motorB.run_target(500, 1800)
    else:
        a = 5
        while color_sensor.reflection() < deciding_value:
            front_motor.run_target(500,a)
            front_motor.run_target(500, -a)
        front_motor.run_target(500,0)
    brick.sound.beep()