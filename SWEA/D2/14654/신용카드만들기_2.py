import sys

sys.stdin = open("./input.txt",'r')

T = int(sys.stdin.readline())
#input 파일 불러오기
for i in range(1,T+1): # Test case 갯수 만큼 반복문 시행
    card_name = sys.stdin.readline() # 파일 읽어오기
    card_name = card_name.replace('-',"") # '-' 가 들어가있는 경우 삭제해주기
    card_name = card_name.strip() # 공백 제거
    if len(card_name) == 16: # 카드 자리수가 16자리 이면 카드가 성립하므로 조건문 생성
        if card_name[0:1] == '3' or card_name[0:1] == '4' or card_name[0:1] == '5' or card_name[0:1] == '6' or card_name[0:1] == '9': # 첫자리가 3,4,5,6,9 일때 카드 생성
            print(f"#{i}", 1)
        else: # 아닐때 0
            print(f"#{i}", 0)
    else: # 16자리가 아닐때도 0
        print(f"#{i}", 0)