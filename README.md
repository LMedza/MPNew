Robotic Whistle
Author: Lukasz Medza lum22@aber.ac.uk
Version: 1.0 (Release)
--------------------------------

For a detailed user manual see 'Appendix C - User Manual' in the final project report. This document is a cut down quick start version of the user guide

Backup MIDI Output
--------------------------------

This is an optional feature and the program will execute and run without it, however it is strongly suggested that a backup output is provided to fill in any gaps in the musical range of the instrument.

A backup output can be either physical (like a MIDI keyboard or a synthesiser) or it can be virtual. By default the program is hardcoded to forward any unplayable notes to channel 129 which should in turn be set as the input channel of your chosen backup device.

For testing purposes this project utilised Timidity. In order to set up Timidity for use here it should be made to run as a daemon where it will act as an ALSA sequencer client. To do this the timidity.service should be enabled. On dedicated machines it is a good idea to make this service run on boot.

Preparing the Hardware
--------------------------------

The Pololu servo controller requires minor calibration before it is made fully operational. By default when plugged into a USB port the device might not work; displaying a green light and a flashing red light meaning that the baudrate of the USB connection is too high. 

The baudrate of a USB port can be checked with the following;  
stty –F /dev/ttyUSB0 

The device itself supports a baudrate in the range of 2,000 to 40,000 with 9600 proving to be sufficient during testing. The baudrate can be easily changed with the following:
stty –F /dev/ttyUSB0 9600

Note; in some cases the baudrate doesn’t update until the next power cycle meaning that the computer has to be put into suspend mode and then re-activated to let the baudrate refresh.

Running the Program
--------------------------------


The program runs two separate components which both need to run at the same time. Firstly; the Python code can be executed with:
python AlsaMain.py

The program will work in the background; but can be checked that it’s working by running the following:
aconnect –o

The input itself is provided via ALSA by running the following command:
aplaymidi --port 129 mymidifile.mid

Running the above will then pass the MIDI file for execution to the Python program where it will be parsed one event at a time and played in real time.
