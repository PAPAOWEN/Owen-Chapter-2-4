currenttime=int(input("what is the current time?"))
waittime=int(input("what is the wait time for the alarm?"))
alarmtime= (currenttime+waittime)%24
print("the time alarm will go off is", alarmtime)