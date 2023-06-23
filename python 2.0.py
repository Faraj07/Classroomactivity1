wind_speeds = [52,24,12,21,11,912,10,23,14,9,11,4122,6,12]
highest = 0
newlist = []
n = 0
highest2 = 0
m = 0

list_of_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

for i in range(len(wind_speeds)):
    if highest < wind_speeds[i]:
        highest = wind_speeds[i]
print("highest one is: ",highest)
for k in range(len(wind_speeds)):
    if wind_speeds[k] == highest:
        print("index of",highest,"is: ", k)
        if (k % 7) == 0:
            in_which_week = int(k / 7)+1
        else:
            in_which_week = int(k//7) + 1

        while n != 7 :
            try:
                newlist.append(wind_speeds[(in_which_week - 1) * 7 + n])
            except:
                pass
            n = n + 1
        for si in range(len(newlist)):
            if highest2 < newlist[si]:
                highest2 = newlist[si]
        for ok in range(len(newlist)):
            if newlist[ok] == highest2:
                print('the exact weekday is: ', list_of_weekdays[ok])


        print(newlist)









