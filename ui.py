#!/usr/bin/env python

import curses 
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Tank Robot v0.1", curses.A_REVERSE)
    stdscr.addstr(1, 0, "Direction : ")
    stdscr.addstr(2, 0, "Speed     : ")

    stdscr.addstr(1, 13, "Forward")
    stdscr.addstr(2, 13, "0")

    while True:
        c = stdscr.getch()
        if c == ord('w'):
            motors.MoveForward()
        elif c == ord("s"):
            motors.MoveBackward()
        elif c == ord("a"):
            motors.TurnLeft()
        elif c == ord("d"):
            motors.TurnRight()
        elif c == ord("q"):
            motors.IncreaseSpeed()
        elif c == ord("e"):
            motors.DecreaseSpeed()
        elif c == ord("r"):
            break

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
                                    #stdscr = curses.initscr()
                                    #don't print keys 
                                    #curses.noecho()
                                    #react instantly 
                                    #curses.cbreak()
                                    #handle special keys 
                                    #stdscr.keypad(True)

                                    #curses.nocbreak()
                                    #stdscr.keypad(False)
                                    #curses.echo()
                                    #curses.endwin()


