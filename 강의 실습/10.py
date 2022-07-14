# > 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
# > 

# ### Input

# ```python
# numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
# ```

# ### Output

# ```
# 3
# ```

def search(a,s_list=[]):
    cnt=0
    for i in s_list:
        if i == a:
            cnt+=1
    return cnt


numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
y = search(5,numbers)
print(y)