char_list = ['a','e','i','o','u','A','E','I','O','U']
while True:
    char = input()
    cnt = 0
    if char == '#':
        break
    else:
        for i in char:
            if i in char_list:
                cnt += 1
        print(cnt)