import alsaseq, sys
from MusicParser import *
from ServoEvent import *
from FreePlay import *

class AlsaMain:
    def main():

        se = ServoEvent()
        parser = MusicParser()
        alsaseq.client('RoboWhistle PassThrough', 1, 1, False)  # Set up a new ALSA channel
        alsaseq.connectfrom(1, 129, 0)  # Midi file input needs to be sent in to channel 129
        # Backup ALSA channel to run on port 128. Can use either a virtual synth (e.g. Timidity or a physical MIDI keyboard)
        alsaseq.connectto(1, 128, 0)

        srv = ServoEvent()
        srv.ResetServoEvent()

        #To enter FreePlay mode provide any argument when running the program; if left blank AutoPlay will proceed automaticlly
        if len(sys.argv) is 2:
                print "Entering FreePlay Mode"
                play = FreePlay()
                play.ManualPlay()
        else:
            print str(len(sys.argv))
            while 1:
                if alsaseq.inputpending():  # ALSA queue
                    event = alsaseq.input()  # Pop event from top of the queue
                    eventPitch = event[7][1]  # Pitch of the note that needs to be played

                    parsedNote = parser.AnalyseSingleNote(eventPitch % 12)

                    if parsedNote is None:
                        alsaseq.output(event)  # Event is unplayable by the whistle, forward it to the synthesiser
                    else:
                        se.PlayNoteEvent(parsedNote)  # Pass item for playing



    if __name__ == "__main__":
        main()

