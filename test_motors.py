#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

mh = Adafruit_MotorHAT(addr=0x70)

print("Get motors")
#left
motor1 = mh.getMotor(1)
#right 
motor4 = mh.getMotor(4)

print("Set motor speed 255")
motor1.run(Adafruit_MotorHAT.FORWARD)
motor4.run(Adafruit_MotorHAT.FORWARD)
#motor1.setSpeed(50)
#motor4.setSpeed(50)
#time.sleep(2)
#motor1.setSpeed(150)
#motor4.setSpeed(150)
#time.sleep(2)
#motor1.setSpeed(200)
#motor4.setSpeed(200)
#time.sleep(2)
motor1.setSpeed(250)
motor4.setSpeed(250)
#time.sleep(2)
#motor1.setSpeed(150)
#motor4.setSpeed(150)
#time.sleep(2)
#motor1.setSpeed(100)
#motor4.setSpeed(100)
#time.sleep(2)
#motor1.setSpeed(50)
#motor4.setSpeed(50)
time.sleep(2)
print("Set motor speed 0")
motor1.setSpeed(0)
motor4.setSpeed(0)

print("release")
motor1.run(Adafruit_MotorHAT.RELEASE)
motor4.run(Adafruit_MotorHAT.RELEASE)

