import curses 
import time
from curses import wrapper
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing Test!") 
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh( )
    stdscr.getkey()

def display_text( stdsrc, target_text,current_text , wpm = 0):
    stdsrc.addstr(target_text,curses.color_pair(3))
    stdsrc.addstr(1,0,f"WPM: {wpm}")
    for i, char in enumerate(current_text):
        if current_text[i] != target_text[i]:
            stdsrc.addstr(0,i,char,curses.color_pair(2))
        else:
            stdsrc.addstr(0,i,char,curses.color_pair(1))

def wpm_test(stdscr):
    TEXT = []
    with open("text.txt", "r") as file:
        lines = file.readlines()  
        for line in lines:
            TEXT.append(line)
    file.close()
    MAX_TEXT = len(TEXT)

    text_no = random.randrange(0,MAX_TEXT)
    target_text = TEXT[text_no]
    target_text = target_text.strip()
    current_text = []
    wpm = 0 
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time.sleep(0.005)
        time_elapsed = max(time.time() - start_time,1)
        wpm =  round((len(current_text)/(time_elapsed/60))/5)
        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
           continue
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        
        elif len(current_text) < len(target_text):
            current_text.append(key)


    
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, "You completed the text! Press any key to Countinue..")
        
        
    
wrapper(main)
