X,Y,W,S = map(int,input().split())

# 직선으로 이동한 거리
s1 = (X+Y)*W

# 대각선으로만 이동한 거리 X,Y의 합이 2의 배수가 아닌경우 홀수로 한칸이 남기때문에 조건을 다르게 해줘야한다.
if (X+Y) % 2 == 0:
    s2 = max(X,Y)*S
else:
# 대각선 이동 + 한칸 이동거리
    s2 = (max(X,Y)-1)*S + W

# 대각선 최대이동 + 나머지 블록이동
s3 = (min(X,Y)*S + (max(X,Y)-min(X,Y))*W)

print(min(s1,s2,s3))