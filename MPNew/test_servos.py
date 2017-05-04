import pytest
from AlsaMain import *

def test_serial_link():
    newMod = AlsaMain()
    assert newMod.se.serialport != None
   # print str(newMod.se.serialport)
