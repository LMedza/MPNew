from MidiNote import *

# Contains the notes physically playable by the whistle, notes given below are for a D whistle but can be swapped out for any key
global playableList
playableList = []


class MusicParser:
    def __init__(self):
       None


    #Takes a MIDI pitch value to analyse  if it is playable
    def AnalyseSingleNote(self, notePitch):
        del playableList[:]
        self.LoadPlayableList("./resources/playable.txt")  #The default file is for a whistle in D


        for item in playableList:
            if notePitch == item.octave_mod:
                if item.holes is None:
                    # Note is unplayable, forward to Timidity
                    print "Note is unplayable, forwarding to channel 128"
                    return None
                else:
                    # Note is playable
                    print "Will play " + str(item.holes) + " " + str(notePitch)
                    return item.holes

    #Loads the list of notes playable in a given key; can be used to easily load in a note set for any key
    def LoadPlayableList(self, path):
        with open(path) as f:
            for line in f:
                BoolConversionList = []
                x = 0

                newstr = line.translate(None, "',()\n[]")
                splitstr = newstr.split(' ')

                #Values read in from the file are strings, this converts them into booleans
                if len(splitstr) > 3:
                    for st in splitstr[2:8]:
                        if st == "True":
                            BoolConversionList.append(True)
                        else:
                            BoolConversionList.append(False)
                else:
                    BoolConversionList = None

                    x = x + 1

                note = MidiNote(int(splitstr[0]), splitstr[1], BoolConversionList)
                playableList.append(note)

        f.close()
