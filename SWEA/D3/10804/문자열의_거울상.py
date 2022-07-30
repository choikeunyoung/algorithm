import sys

sys.stdin = open("./input.txt", "r")

T = int(sys.stdin.readline())
# input 파일 받아오기
for i in range (1,T+1): # Test case 갯수만큼 반복
    char_dict={} # dictionary 선언
    cnt = 0
    char = sys.stdin.readline() # 들어온 문자 받아들이기
    char = char.strip() # 공백 제거
    for j in char: # 들어온 문자들을 반복
        if j in char_dict: #dictionary 에 존재하는지 안하는지 판단
            pass
        else: # 존재 하지 않으면 b 는 d로 p 는 q 로 반환
            if j == "b":
                char_dict[j] = "d"
            elif j == 'd':
                char_dict[j] = 'b'
            elif j == 'p':
                char_dict[j] = 'q'
            elif j == 'q':
                char_dict[j] = 'p'
    print(f'#{i}', end=" ") # 입출력 형식 맞추는 용도
    for k in char[::-1]: # 문자열 역순으로 반복문 시행
        print(char_dict[k], end="") # 역순으로 값들을 딕셔너리에 넣어서 반환해줌
        cnt += 1
        if cnt == len(char): # cnt를 세어줘서 한 문자가 끝날경우 종료
            print()
            break

# T = int(input())

# for i in range (1,T+1):
#     char_dict={}
#     cnt = 0
#     char = input()
#     char = char.strip()
#     for j in char:
#         if j in char_dict:
#             pass
#         else:
#             if j == "b":
#                 char_dict[j] = "d"
#             elif j == 'd':
#                 char_dict[j] = 'b'
#             elif j == 'p':
#                 char_dict[j] = 'q'
#             elif j == 'q':
#                 char_dict[j] = 'p'
#     print(f'#{i}', end=" ")
#     for k in char[::-1]:
#         print(char_dict[k], end="")
#         cnt += 1
#         if cnt == len(char):
#             print()
#             break
