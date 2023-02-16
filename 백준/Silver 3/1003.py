# def fibonacci(num):
#     if num == 0:
#         return 
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1)
n=int(input())
score=list(map(int,input().split()))
m=max(score)
sum=0
for i in score:
    sum+=(i/m*100)
print(sum/n)