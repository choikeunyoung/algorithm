# answer = input()
# # 1부터 ~ N 까지 값 변수
# cnt = 1
# # 리스트 인덱스
# index = 0
# # 언제까지 반복할지 모르기때문에 while
# while True:
#     # 10 이상일 경우 자리수마다 나눠서 값을 비교해야기 때문에
#     if cnt >= 10:
#         # 두자리 수 이상일 경우 각 자리마다 값 체크
#         for j in str(cnt):
#             # 만약 값이 인덱스값과 같은 경우 인덱스 증가
#             if int(j) == int(answer[index]):
#                 index += 1
#             # 증가한 인덱스가 끝인경우 break
#             if index == len(answer):
#                 break
#     else:
#         # 한자리 수가 인덱스 값과 같은 경우 인덱스 증가
#         if cnt == int(answer[index]):
#             index += 1
#     # 인덱스가 끝인 경우 1씩 증가한 값 중 cnt 값 출력
#     if index == len(answer):
#         print(cnt)
#         break
#     cnt += 1


num = "start1234"
print(intsum(num))