from collections import deque

N = int(input())

words = deque(map(str,input()))

m_cnt = 0
w_cnt = 0

while words:
    # 리스트 값을 왼쪽부터 뽑으면서
    check = words.popleft()
    # 남자면 m_cnt 1 증가
    if check == "M":
        m_cnt += 1
    # 여자면 w_cnt 1 증가
    elif check == "W":
        w_cnt += 1
    # 만약 두 값의 차가 N 보다 큰 경우
    if max(m_cnt, w_cnt) - min(m_cnt, w_cnt) > N:
        # 리스트가 존재하면
        if words:
            # 값을 한개 더 뽑아본다
            middle_check = words.popleft()
            # m_cnt 값이 w_cnt 값보다 큰 경우
            if m_cnt > w_cnt:
                # m_cnt 값이 위에서 증가됐기 때문에 1 뺀다
                m_cnt -= 1
                # 한개 더 뽑은 값이 W 인 경우
                if middle_check == "W":
                    # w_cnt 값 1 증가
                    w_cnt += 1
                    # M 값이였던 check 값을 리스트에 왼쪽에 더해줌
                    words.appendleft(check)
                # M 인 경우 반복문 종료
                else:
                    break
            # m_cnt 값이 w_cnt 값보다 작은 경우
            elif m_cnt < w_cnt:
                # w_cnt 값 -1
                w_cnt -= 1
                # 한개 더 뽑은 값이 M 인 경우
                if middle_check == "M":
                    # m_cnt 값 1 증가
                    m_cnt += 1
                    # check 값을 리스트에 왼쪽 값에 증가
                    words.appendleft(check)
                else:
                    break
        # 리스트가 없으면
        else:
            # N 값보다 컸을 때 경우이기 때문에
            if m_cnt > w_cnt:
                # 뽑은 값이 M 이였으면 +1 을 해줬기 떄문에 -1
                if check == "M":
                    m_cnt -= 1
            elif m_cnt < w_cnt:
                # 뽑은 값이 W 였으면 +1 을 해줬기 때문에 -1
                if check == "W":
                    w_cnt -= 1
            break
# 반복문이 끝나면 계산한 여자와 남자들이 들어간 갯수 더해줌
print(w_cnt + m_cnt)