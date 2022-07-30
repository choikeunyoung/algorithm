import sys

sys.stdin = open("./input.txt", 'r')
# input 파일 불러오기

for i in range(1,11): # 테스트 케이스 10개여서 range 10으로 설정
    origin = int(sys.stdin.readline()) # origin 의 문자길이 받기
    origin_pass = list(map(str,sys.stdin.readline().split())) # 원본 암호 데이터
    admin = int(sys.stdin.readline()) # 수정할 데이터 길이
    admin_pass = list(map(str,sys.stdin.readline().split())) # 수정해야 하는 양식
    check_position = [] # I 값을 기준으로 코드를 작성할 예정이라 I위치 체크하는 리스트 생성
    for k in admin_pass: # I 값의 위치를 check_position 리스트에 추가
        if k == "I":
            check_position.append(1)
        else:
            check_position.append(0)
    
    for l in range(0,len(check_position)): # 추가된 I 값의 위치 리스트에서
        if check_position[l] == 1: 
            insert_pos= int(admin_pass[l+1]) # I를 기준으로 +1 칸에는 원본에서 넣고싶은 위치
            count_num = int(admin_pass[l+2]) # I를 기준으로 +2 칸에는 넣고싶은 숫자의 갯수
            list_num = admin_pass[l+3:l+3+count_num] # I를 기준으로 넣어야 하는 숫자들의 리스트
            for j in range(0,len(list_num)): # 넣고싶은 숫자들의 리스트 내부에서 반복문 돌림
                origin_pass.insert(insert_pos+j,list_num[j]) # 넣을 위치는 insert_pos 로 설정하였고 계속 삽입이 되기때문에 위치를 +j 씩 해줘야한다.
    print(f'#{i} ', end='') #출력문 양식
    for n in range(0,10):
        print(int(origin_pass[n]), end=' ') #앞에서부터 10개를 구하라 하였으니 range 10설정
    print() #출력문 양식