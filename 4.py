S = int(input())
hour = int(S / 3600)
minute = int((S-hour*3600)/60)
second = S-hour*3600-minute*60
print(str(hour)+":"+str(minute)+":"+str(second))