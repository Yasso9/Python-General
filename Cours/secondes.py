time = 50000000

second = time % 60
time = (time - second) / 60

minute = time % 60
time = (time - minute) / 60

hour = time % 24
time = (time - hour) / 24

day = time % 30
time = (time - day) / 30

month = time % 12
time = (time - month) / 12

year = time


print("date :", day, month, year, "  time :", hour, minute, second)