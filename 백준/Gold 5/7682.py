while True:
    game = input()
    if game == "end":
        break

    game = list(map(str,game))

    circle = game.count("O")
    cross = game.count("X")
    dot = game.count(".")
    if circle > cross:
        print("invalid")
    else:
        if cross - circle > 1:
            print("invalid")
        else:
            matrix = [ game[:3], game[3:6], game[6:]]
            for i in range(3):
                cross_flag = 0
                circle_flag = 0
                cross_check = 0
                circle_check = 0
                # 대각 선 범위 체크
                if i == 0:
                    if matrix[i][0] == "X":
                        if matrix[i+1][1] == "X":
                            if matrix[i+2][2] == "X":
                                cross_flag = 1
                    elif matrix[i][0] == "O":
                        if matrix[i+1][1] == "O":
                            if matrix[i+2][2] == "O":
                                circle_flag = 1
                    if matrix[i][2] == "X":
                        if matrix[i+1][1] == "X":
                            if matrix[i+2][0] == "X":
                                cross_flag = 1
                    elif matrix[i][2] == "O":
                        if matrix[i+1][1] == "O":
                            if matrix[i+2][0] == "O":
                                circle_flag = 1
                    if matrix[i][0] == "X":
                        if matrix[i+1][0] == "X":
                            if matrix[i+2][0] == "X":
                                cross_flag = 1
                    elif matrix[i][0] == "O":
                        if matrix[i+1][0] == "O":
                            if matrix[i+2][0] == "O":
                                circle_flag = 1
                    if matrix[i][1] == "X":
                        if matrix[i+1][1] == "X":
                            if matrix[i+2][1] == "X":
                                cross_flag = 1
                    elif matrix[i][1] == "O":
                        if matrix[i+1][1] == "O":
                            if matrix[i+2][1] == "O":
                                circle_flag = 1
                    if matrix[i][2] == "X":
                        if matrix[i+1][2] == "X":
                            if matrix[i+2][2] == "X":
                                cross_flag = 1
                    elif matrix[i][2] == "O":
                        if matrix[i+1][2] == "O":
                            if matrix[i+2][2] == "O":
                                circle_flag = 1
                # 가로 개수 체크
                for j in range(3):
                    circle_check = matrix[j].count("O")
                    cross_check = matrix[j].count("X")
                    if circle_check == 3:
                        circle_flag = 1

                    if cross_check == 3:
                        cross_flag = 1
                # X 빙고일 경우 O 빙고가 있는지 체크
                if cross_flag == 1:
                    if circle_flag != 1:
                        # X 빙고의 경우 O의 개수가 작아야 하는거 체크
                        if cross > circle:
                            print("valid")
                        else:
                            print("invalid")
                    else:
                        print("invalid")
                    break
                # O 빙고의 경우 X 빙고가 있는지 체크
                if circle_flag == 1:
                    if cross_flag != 1:
                        # O 빙고의 경우 꽉차있는 경우 나올 수 없으므로 체크
                        if dot == 0:
                            print("invalid")
                        else:
                            #  꽉 차있지 않는 경우 X와 O의 개수가 같아야 하기 떄문에 체크
                            if cross == circle:
                                print("valid")
                            else:
                                print("invalid")
                    else:
                        print("invalid")
                    break
            else:
                # 모든 경우를 통과했을때 꽉 차있는지 체크
                if dot == 0:
                    if cross == 5 and circle == 4:
                        print("valid")
                        continue
                print("invalid")
