before,after = list(map(int,input().split()))

if before % 4 == 0:
    before_val = before//4 - 1
    before_val_nam = 4
else:
    before_val = before//4
    before_val_nam = before%4
if after % 4 == 0:
    after_val = after//4 - 1
    after_val_nam = 4
else:
    after_val = after//4
    after_val_nam = after%4

print(abs(after_val - before_val) + abs(after_val_nam - before_val_nam))