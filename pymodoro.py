#!/usr/bin/python

import argparse
import time
import threading
import sys
from blessed import Terminal

parser = argparse.ArgumentParser()
parser.add_argument('-wm', type=float, help='Working minutes')
parser.add_argument('-bm', type=float, help='Break minutes')
parser.add_argument('start', help='Start timer')

timeLeft = 25

inputChar = ''          # Character to be used to eventually stop the program
t = Terminal()


def quitPomodoro():
    sys.exit()

def printStatus():
    print(t.center("", fillchar="@"))
    print("@" + t.move_right(t.width) + "@")
    print(t.center(f"    Time remaining: {t.bold + str(timeLeft)}    ", fillchar="~"))
    print("@" + t.move_right(t.width) + "@")
    print(t.center("", fillchar="@"))
    print(t.move_up(6))


def checkInput():
    """
    Loop that gets the input character in the terminal every second.
    """
    global inputChar
    with t.hidden_cursor():     # Hide cursor
        with t.cbreak():
            while True:
                inputChar = t.inkey(timeout=1)


def loop():
    global timeLeft
    while timeLeft >= 0 and inputChar.lower() != 'q':
        try:
            printStatus()
            timeLeft -= 1
            time.sleep(1)
        except (KeyboardInterrupt, Exception):
            quitPomodoro()
    quitPomodoro()


def main():
    inputThread = threading.Thread(target=checkInput)
    inputThread.daemon = True
    
    inputThread.start()
    loop()

if __name__ == "__main__":
    main()