# > 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# **sum() 함수 사용 금지**
# > 

# ### Input

# ```python
# n = 10
# ```

# ### Output

# ```
# 55
# ```

n = int(input())
a = 0
while n!=0:
    a += n
    n -= 1
print(a)

n = int(input())
b = 0
for i in range(1,n+1):
    b += i

print(b)