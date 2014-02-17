
#easy method
month_days = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}

week = [0]*8

def counter_week(  ):
    t = 1
    for i in range (1901, 2001):
        print "Year-%d,"%(i),
        for j in range(1, 13):
            days = month_days[j]
            if j == 2 and ((i % 4 == 0 and i % 100 != 0) or i % 400 == 0):
                days = days + 1
#            print "%d-%d,"%(j, days),
            for k in range (1, days):
                if k == 1 and i != 1900:
                    week[t] = week[t] + 1
                t = t + 1
                if t == 8:
                    t = 1
        print ''

counter_week()                    
for i in range( 1, 8 ):
    print "%d-%d, "%(i, week[i]),
print ''    
    
    
#Zeller’s Formula
#    
def day_of_week( year, month, day ):
    if month == 1 or month == 2:
        year = year - 1
        month = month + 12
    y = year % 100
    c = year / 100
    week = (y + y/4 + c/4 - 2*c + 26*(month+1)/10 + day - 1) % 7
    if week < 0:
        week = (week + 7)%7
    return week

sunday = 0    
for i in range(1901, 2001):
    for j in range (1, 13):
        if day_of_week( i, j, 1 ) == 0:
            sunday = sunday + 1

print sunday