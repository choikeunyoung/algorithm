# > 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# **sum(), len()  함수 사용 금지**
# > 

# ### Input

# ```python
# numbers = [3, 10, 20]
# ```

# ### Output

# ```
# 11.0
# ```

numbers = [3, 10, 20]
cnt = 0
total = 0
for i in numbers:
    total +=i
    cnt+=1
print(total)
print(total//cnt)