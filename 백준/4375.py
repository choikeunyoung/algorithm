while True:
    try:
        n = input()
        check = "1"
        if n == "":
            break
        else:
            while True:
                if (int(check) < int(n)):
                    check += "1" # "11"
                    continue
                else:
                    if (int(check)%int(n)) == 0:
                        print(len(check))
                        break
                    else:
                        check += "1"
    except EOFError:
        break