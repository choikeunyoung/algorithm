# > 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# > 

# ### Input

# ```
# banana
# ```

# ### Output

# ```python
# b 1
# a 3
# n 2
# ```

# ## 접근 방법

# dict에 값들을 추가해 가며 더해나가는 방식으로 진행

word = input()

my_dict = {}

for i in word:
    if my_dict.get(i) != None:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
    
for v, k in my_dict.items():
    print(v, k)