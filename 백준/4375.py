while True:
    try:
        n = input()
        cnt = 0
        ans = 0
        check = "1"
        if n == "":
            break
        else:
            while True:
                if (int(check) < int(n)):
                    check += "1"
                    continue
                else:
                    if (int(check)%int(n)) == 0:
                        print(len(check))
                        break
                    else:
                        check += "1"
    except EOFError:
        break