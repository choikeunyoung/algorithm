while True:
    infos = list(map(str,input().split()))
    if infos[0] == "#":
        break
    else:
        if int(infos[1]) > 17 or int(infos[2]) >= 80:
            print(infos[0],"Senior")
        else:
            print(infos[0],"Junior")