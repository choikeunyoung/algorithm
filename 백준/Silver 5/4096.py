while True:
    num = input()
    if num == "0":
        break
    else:
        num_length = len(num)
        if num_length % 2 == 0:
            meter = num[:num_length//2]
            meter = meter[::-1]
            need = num[num_length//2:]
            meter_length = len(meter)
            if int(meter) > int(need):
                print(int(meter)-int(need))
            elif int(meter) == int(need):
                print(0)
            else:
                meter = meter[::-1]
                meter = str(int(meter)+1)
                meter = meter[::-1]
                answer_number = 10**meter_length
                answer = answer_number - int(need)
                if len(meter) < meter_length:
                    meter = meter[::-1]
                    meter += "0"*(meter_length-len(meter))
                answer += int(meter)
                print(answer)
        else:
            meter = num[:num_length//2]
            middle = num[num_length//2]
            meter = meter[::-1]
            need = num[(num_length//2)+1:]
            meter_length = len(meter)
            if int(meter) > int(need):
                print(int(meter)-int(need))
            elif int(meter) == int(need):
                print(0)
            else:
                if middle == "9":
                    meter = meter[::-1]
                    meter = str(int(meter)+1)
                    meter = meter[::-1]
                    print((10**meter_length)-int(need)+int(meter))
                else:
                    answer_number = 10**meter_length
                    answer = answer_number - int(need)
                    if len(meter) < meter_length:
                        meter = meter[::-1]
                        meter += "0"*(meter_length-len(meter))
                    answer += int(meter)
                    print(answer)