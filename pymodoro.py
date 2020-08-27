#!/usr/bin/env python3

from blessed import Terminal
import argparse
import time
import threading
import sys
import warnings
from utils import getRemainingTime, minutesToSeconds, printMessage

warnings.filterwarnings('ignore')
parser = argparse.ArgumentParser()
parser.add_argument('-w', type=float, help='Working minutes')
parser.add_argument('-b', type=float, help='Break minutes')
parser.add_argument('start', help='Start timer')
args = parser.parse_args()

inputChar = ''          # Character to be used to eventually stop the program
t = Terminal()

timeLeft = minutesToSeconds(args.w)
isBreak = False

def quitPomodoro():
    print('\n'*10)
    sys.exit()


def getInput():
    """
    Loop that continuously takes input from the terminal
    """
    global inputChar
    while True:
        inputChar = t.inkey()

def askForConfirmation(message):
    answer = ""
    while answer.lower() != "y" and answer.lower() != "n":
        printMessage(f"{message}(y/n): ", terminal=t)
        answer = t.inkey(timeout=60)
    return answer.lower() == "y"


def loop():
    global timeLeft
    global isBreak
    prefix = "BREAK" if isBreak else "WORKING"

    with t.cbreak(), t.hidden_cursor():
        while timeLeft >= 0 and inputChar.lower() != 'q':
            try:
                printMessage(f"[{prefix}]: Time remaining: {t.bold + getRemainingTime(timeLeft)}", terminal=t)
                timeLeft -= 1
                time.sleep(1)
            except (KeyboardInterrupt, Exception):
                quitPomodoro()

        if(inputChar.lower() != 'q'):
            if isBreak and askForConfirmation("Start working again?"):
                isBreak = False
                timeLeft = minutesToSeconds(args.w)
                loop()
                
            elif askForConfirmation("Time is up. Start break?"):
                isBreak = True
                timeLeft = minutesToSeconds(args.b or 5)
                loop()
        quitPomodoro()


def main():
    inputThread = threading.Thread(target=getInput)
    inputThread.daemon = True
    
    inputThread.start()
    loop()

if __name__ == "__main__":
    main()