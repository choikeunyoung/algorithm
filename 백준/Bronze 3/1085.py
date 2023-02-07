x,y,w,h = map(int,input().split())
# 0,0 과 w,h 중 제일 가까운 거리의 값을 출력
ans_list = [w-x,h-y,x-0,y-0]
print(min(ans_list))