import pytest
from AlsaMain import *
from ServoEvent import *

def test_serial_connection():
    newMod = ServoEvent()
    assert newMod.serialport.port == "/dev/ttyUSB0"

def test_serial_baudrate():
    newMod = ServoEvent()
    assert newMod.serialport.baudrate == 9600

def test_set_serial_speed():
    newMod = ServoEvent()
    testMod = newMod.SetupSerial(2,80)
    assert testMod.serialspeed != None