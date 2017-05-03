import curses
from ServoEvent import *


class FreePlay:
    def __init__(self):
        return None
    def ManualPlay(self):
        n1 = False
        n2 = False
        n3 = False
        n4 = False
        n5 = False
        n6 = False
        servo = ServoEvent()

        stdscr = curses.initscr()

        while 1:
            c = stdscr.getch()
            if c == ord('a'):
                if n1 == False:
                    servo.NoteOnEvent(2)
                    n1 = True
                else:
                    servo.NoteOffEvent(2)
                    n1 = False
            elif c == ord('s'):
                if n2 == False:
                    servo.NoteOnEvent(3)
                    n2 = True
                else:
                    servo.NoteOffEvent(3)
                    n2 = False
            elif c == ord('d'):
                if n3 == False:
                    servo.NoteOnEvent(4)
                    n3 = True
                else:
                    servo.NoteOffEvent(4)
                    n3 = False
            elif c == ord('h'):
                if n4 == False:
                    servo.NoteOnEvent(5)
                    n4 = True
                else:
                    servo.NoteOffEvent(5)
                    n4 = False
            elif c == ord('j'):
                if n5 == False:
                    servo.NoteOnEvent(6)
                    n5 = True
                else:
                    servo.NoteOffEvent(6)
                    n5 = False
            elif c == ord('k'):
                if n6 == False:
                    servo.NoteOnEvent(7)
                    n6 = True
                else:
                    servo.NoteOffEvent(7)
                    n6 = False


            elif c == ord('q'):
                break