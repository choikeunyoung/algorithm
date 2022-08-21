problems = []
start = input()
if start == "고무오리 디버깅 시작":
    while True:
        A = input()
        if A == "문제":
            problems.append(A)
        elif A == "고무오리" and len(problems) == 0:
            problems.append('문제')
            problems.append('문제')
        elif A == "고무오리" and len(problems) > 0:
            problems.pop()
        elif A == "고무오리 디버깅 끝":
            if len(problems) > 0:
                print("힝구")
                break
            else:
                print("고무오리야 사랑해")
                break