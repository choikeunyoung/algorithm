# > 문자열 word가 주어질 때, 해당 문자열에서 `a` 의 모든 위치(index)를 출력해주세요.
# **`find()` `index()` 메서드 사용 금지**
# > 

# ### Input

# ```
# HappyHacking
# ```

# ### Output

# ```
# 1 6
# ```

# 아래의 테스트 케이스로도 확인 해보세요.

# ```python
# banana # 1 3 5
# kiwi # 
# ```

word = input()
check_list=[]
for i in range(0,len(word)):
    if word[i]=="a":
        check_list.append(i)
    else:
        check_list.append(0)

for i in check_list:
    if i > 0:
        print(check_list[i], end=" ")