import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(sys.stdin.readline())

grade = {
    1 : "A+",
    2 : "A0",
    3 : "A-",
    4 : "B+",
    5 : "B0",
    6 : "B-",
    7 : "C+",
    8 : "C0",
    9 : "C-",
    10 : "D0"
}

for i in range (1,T+1):
    n,y = list(map(int,sys.stdin.readline().split()))
    total_list=[]
    for k in range(n):
        score = list(map(int,sys.stdin.readline().split()))
        for l in range(0,len(score)):
            if l == 0:
                score[l] = round(score[l]*0.35,1)
            elif l == 1:
                score[l] = round(score[l]*0.45,1)
            elif l == 2:
                score[l] = round(score[l]*0.2,1)
        total_list.append(sum(score))
    search_ = total_list[y-1]
    total_list.sort(reverse=True)
    search_2 = total_list.index(search_)
    same = n/10
    total_score=[]
    for x in range(0,n):
        total_score.append(grade[x//same+1])
    print(f"#{i} {total_score[search_2]}")