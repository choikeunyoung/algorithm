import collections
from gc import collect
import sys
from collections import Counter
N = int(sys.stdin.readline())
card_list=list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
match_list=list(map(int,sys.stdin.readline().split()))

cnt = Counter(card_list)
print(cnt)
for k in match_list:
    if k in cnt:
        print(cnt[k], end=' ')
    else:
        print('0', end=' ')