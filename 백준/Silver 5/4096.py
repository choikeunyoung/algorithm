# while True:
#     num = input()
#     if num == "0":
#         break
#     else:
#         num_length = len(num)
#         if num_length % 2 == 0:
#             meter = num[:num_length//2]
#             meter = meter[::-1]
#             need = num[num_length//2:]
#             meter_length = len(meter)
#             if int(meter) > int(need):
#                 print(int(meter)-int(need))
#             elif int(meter) == int(need):
#                 print(0)
#             else:
#                 meter = meter[::-1]
#                 meter = str(int(meter)+1)
#                 meter = meter[::-1]
#                 answer_number = 10**meter_length
#                 answer = answer_number - int(need)
#                 if len(meter) < meter_length:
#                     meter = meter[::-1]
#                     meter += "0"*(meter_length-len(meter))
#                 answer += int(meter)
#                 print(answer)
#         else:
#             meter = num[:num_length//2]
#             middle = num[num_length//2]
#             meter = meter[::-1]
#             need = num[(num_length//2)+1:]
#             meter_length = len(meter)
#             if int(meter) > int(need):
#                 print(int(meter)-int(need))
#             elif int(meter) == int(need):
#                 print(0)
#             else:
#                 if middle == "9":
#                     meter = meter[::-1]
#                     meter = str(int(meter)+1)
#                     meter = meter[::-1]
#                     if len(meter) < meter_length:
#                         meter += "0"
#                     print((10**meter_length)-int(need)+int(meter))
#                 else:
#                     answer_number = 10**meter_length
#                     answer = answer_number - int(need)
#                     if len(meter) < meter_length:
#                         meter = meter[::-1]
#                         meter += "0"*(meter_length-len(meter))
#                     answer += int(meter)
#                     print(answer)

while True:
    num = input()
    # input 값이 0 이면 반복문 탈출
    if num == "0":
        break
    else:
        # 몇번 더했는지 확인하는 변수
        cnt = 0
        # 초기의 길이를 체크
        num_length = len(num)
        # 1씩 계속 더해나감
        while True:
            # 앞뒤가 같은지 확인
            if num[::] == num[::-1]:
                # 같으면 몇번 더했는지 출력
                print(cnt)
                break
            # 아닐경우
            else:
                # 이전의 값에 1을 계속 더해나감
                num = str(int(num) + 1)
                # 만약 길이가 처음 길이보다 작아졌을 경우 앞에 0을 차이만큼 추가해줌
                if len(num) < num_length:
                    num = num[::-1]
                    num += "0"*(num_length-len(num))
                    num = num[::-1]
            cnt += 1