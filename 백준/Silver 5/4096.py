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
            print(int(meter),int(need))
            if int(meter) > int(need):
                print(int(meter)-int(need))
            elif int(meter) == int(need):
                print(0)
            else:
                answer_number = 10**meter_length
                answer_number = answer_number - int(meter)
                answer = answer_number - int(need)
                print(answer,answer_number)
        else:
            pass