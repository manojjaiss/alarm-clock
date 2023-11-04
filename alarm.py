import datetime
from playsound import playsound

alarmHour = int(input("enter Hour:"))
alarmMinute = int(input("Enter Minute : "))
alarmAm = input("am/pm:")

if alarmAm == "pm":
    alarmHour += 12

def play_alarm():
    print("playing..")
    playsound("mixkit-classic-alarm-995.wav")

def alarm_time():
    return alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute

while True:
    if alarm_time():
        play_alarm()
        break
     