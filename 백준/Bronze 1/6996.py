T = int(input())

for i in range(T):
    A,B = map(str,input().split())
    C = sorted(A)
    D = sorted(B)
    if C == D:
        print(f"{A} & {B} are anagrams.")
    else:
        print(f"{A} & {B} are NOT anagrams.")