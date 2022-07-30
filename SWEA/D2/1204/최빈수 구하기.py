import sys

sys.stdin = open("./input.txt",'r')

T = int(sys.stdin.readline())
# input 파일 불러오기

for i in range(1,T+1): # Test case 갯수만큼 반복
    num_dict={} # dictionary 선언
    j = int(sys.stdin.readline()) # 한줄 씩 읽어들임
    num_list = list(map(str,sys.stdin.readline().split())) # list 형태로 저장
    for k in num_list: # list 내부 탐색
        if k in num_dict: # dictionary 내에 존재할 경우 그 value 값 +1
            num_dict[k] += 1
        else: # dctionary 내부에 없을 경우 그 값과 횟수를 1로 저장
            num_dict[k] = 1
    
    for k,v in num_dict.items(): # key, value로 나뉘어
        if max(num_dict.values()) == v: # value 값이 max 일때 key 출력
            print(f"#{j}",k)