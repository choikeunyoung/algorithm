# > 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# `**count()` 사용 금지**
# > 

# ### Input

# ```
# apple
# ```

# ### Output

# ```
# 2
# ```

# 아래의 테스트 케이스로도 확인 해보세요.

# ```python
# aeiou # 5
# zxcvb # 0
# ```

word = input()

mo_list=['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in word:
    if i in mo_list:
        cnt +=1

print(cnt)