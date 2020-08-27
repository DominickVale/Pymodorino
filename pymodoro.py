#!/usr/bin/env python3

from blessed import Terminal
import argparse
import time
import threading
import sys
import warnings

warnings.filterwarnings('ignore')
parser = argparse.ArgumentParser()
parser.add_argument('-w', type=float, help='Working minutes')
parser.add_argument('-b', type=float, help='Break minutes')
parser.add_argument('start', help='Start timer')
args = parser.parse_args()

inputChar = ''          # Character to be used to eventually stop the program
t = Terminal()

timeLeft = 60 * args.w


def quitPomodoro():
    print('\n'*10)
    sys.exit()

def printStatus():
    print('\n\n')
    print(t.center("", fillchar="@"))
    print("@" + t.move_right(t.width) + "@")
    print(t.center(f"    Time remaining: {t.bold + str(timeLeft)}    ", fillchar="~"))
    print("@" + t.move_right(t.width) + "@")
    print(t.center("", fillchar="@"))
    print("\033[9A")


def checkInput():
    """
    Loop that gets the input character in the terminal every second.
    """
    global inputChar
    while True:
        inputChar = t.inkey()


def loop():
    global timeLeft
    with t.cbreak(), t.hidden_cursor():     # Hide cursor
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