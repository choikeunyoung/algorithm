import sys

sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline())

for _ in range(1,T+1):
    all_day = str(sys.stdin.readline())
    year = all_day[0:4]
    month = all_day[4:6]
    day = all_day[6:]
    if int(month) > 12:
        print(f"#{_}", -1)
    elif int(month) ==0:
        print(f"#{_}", -1)
    else:
        if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
            if int(day) > 31:
                print(f"#{_}", -1)
            else:
                print(f"#{_}", end=' ')
                print(year,month,day,sep='/', end='')
        elif int(month) == 2:
            if int(day) >28:
                print(f"#{_}", -1)
            else:
                print(f"#{_}", end=' ')
                print(year,month,day,sep='/', end='')
        else:
            if int(day) >30:
                print(f"#{_}", -1)
            else:
                print(f"#{_}", end=' ')
                print(year,month,day,sep='/', end='')