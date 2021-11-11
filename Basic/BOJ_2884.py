import sys
h, m = map(int, input().split())
hour = []
for i in range(0,24):
    hour.append(i)

alarmM = m - 45
if(alarmM<0):
    h = hour[h-1]
    m = 60 + alarmM

else:
    m = alarmM

print(str(h)+" "+str(m))