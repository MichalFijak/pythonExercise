import time
import pygame
import datetime
import os


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    alarm_path = os.path.dirname(__file__)
    alarm_path = os.path.join(alarm_path, "alarms/Imperial-March-Star-Wars.wav")
    
    pygame.mixer.init()
    pygame.mixer.music.load(alarm_path)    

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm ringing!")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            pygame.mixer.music.stop()
            is_running = False
            break
        time.sleep(1)
        print(f"Current time: {current_time}")

if __name__ == "__main__":
    # Initialize pygame mixer
    # Get the current time and set the alarm time
    alarm_time = input("Set the alarm time (HH:MM:SS): ")

    # Set the alarm
    set_alarm(alarm_time)

    # Wait for the alarm time to be reached
