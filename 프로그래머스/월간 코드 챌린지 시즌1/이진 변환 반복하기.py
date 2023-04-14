def solution(s):
    zero_cnt = 0
    cnt = 1
    while True: 
        check = ""
        print(cnt,s)
        for i in s:
            if i == "0":
                zero_cnt += 1
            elif i == "1":
                check += i
        s_length = len(check)
        if s_length == 1:
            break
        binary_list = []
        while s_length>0:
            binary_list.append(s_length%2)
            s_length //=2
        print(binary_list)
        check = ""
        for j in binary_list[::-1]:
            check += str(j)
        print(check)
        s = check
        cnt += 1
    answer = [cnt, zero_cnt]
    return answer