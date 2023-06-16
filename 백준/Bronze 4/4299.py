hap, cha = map(int,input().split())

answer = hap + cha

team_1 = answer//2
team_2 = hap-team_1

if (team_1 >= 0 and team_2 >= 0) and answer%2 == 0:
    print(team_1,team_2)
else:
    print(-1)