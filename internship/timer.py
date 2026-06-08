from playsound3 import playsound
import time

CLEAR = "\033[2J" #This ANSI used for clearing the terminal
CLEAR_AND_RETURN = "\033[H"#It clear what ever is prited on that line and print

def playAlaram():
    playsound("music.mp3")

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left//60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    playAlaram()
        
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = seconds + (minutes * 60)
alarm(total_seconds)