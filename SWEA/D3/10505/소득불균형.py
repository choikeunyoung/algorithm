import sys

sys.stdin = open("./input.txt","r")

T = int(sys.stdin.readline())
# input 파일 불러오기
for i in range(1,T+1): # Test case 갯수만큼 반복
    N = int(sys.stdin.readline()) # 파일 읽어오기
    get_list = list(map(int,sys.stdin.readline().split())) # list 형태로 저장
    cnt = 0 # 횟수 세기
    get_avg = sum(get_list)//len(get_list) # 평균구하는 방법을 list 의 합 // list 의 길이
    for l in get_list: # list 탐색하며 평균 값보다 작은 갯수를 세준 후 출력
        if l <= get_avg:
            cnt+=1
    print(f"#{i}", cnt)