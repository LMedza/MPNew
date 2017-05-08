import serial

# Handles the physical movement of servos; provides low level instructions over serial
class ServoEvent:



    def __init__(self):
        global serialport

        # Usually USB0 is the default but sometimes the OS can get confused and see the device as USB1
        try:
            serialport = serial.Serial("/dev/ttyUSB0")
        except serial.serialutil.SerialException:
            serialport = serial.Serial("/dev/ttyUSB1")

        serialport.baudrate = 9600  #The baudrate of the servo board serial connection needs to be much lower than most USB devices
        # 9600 seems to work well; this can be bumped up further. See the Pololu servo board user manual for mode info

        self.serialport = serialport

    # Set up the serial connection
    def SetupSerial(self, servo, speed):
        self.serialspeed = chr(0x80) + chr(0x01) + chr(0x01) + chr(servo) + chr(speed)
        serialport.write(self.serialspeed)

        return self

    # Resets all the servos by moving them to the open position (hard coded 90 degrees)
    def ResetServoEvent(self):
        b1 = 3000 & 127
        b2 = (3000 - (3000 & 127)) / 128

        for i in range(0x02, 0x09):
            resetinstruction = chr(0x80) + chr(0x01) + chr(0x04) + chr(i) + chr(b2) + chr(b1)
            serialport.write(resetinstruction)
            i = i + 0x01

    # Moves the servo finger down to cover the hole (hard coded 75 degrees)
    def NoteOnEvent(self, servo):
        if servo < 2:
            servo = servo + 2

        b1 = 2583 & 127
        b2 = (2583 - (2583 & 127)) / 128

        resetinstruction = chr(0x80) + chr(0x01) + chr(0x04) + chr(servo) + chr(b2) + chr(b1)
        serialport.write(resetinstruction)



    # Moves the servo figer up to open the hole (hard coded 90 degrees)
    def NoteOffEvent(self, servo):
        if servo < 2:
            servo = servo + 2

        b1 = 3000 & 127
        b2 = (3000 - (3000 & 127)) / 128

        resetinstruction = chr(0x80) + chr(0x01) + chr(0x04) + chr(servo) + chr(b2) + chr(b1)
        serialport.write(resetinstruction)


    def PlayNoteEvent(self, holesList):
        i = 0
        while len(holesList) > 0:
            item = holesList[0]
            del holesList[0]
            self.NoteOnEvent(15)
            if item:
                self.NoteOnEvent(i+2)
                print str(i + 2) + " ON"
                i = i + 1
            else:
                self.NoteOffEvent(i+2)
                print str(i + 2) + " OFF"
                i = i + 1

        #Stuff happens here for each note played
        # i = 0
        self.NoteOffEvent(15)
