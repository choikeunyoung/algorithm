k = int(input())

for i in range(k):
    class_info = list(map(int,input().split()))
    class_num = class_info.pop(0)
    class_info.sort(reverse=True)
    differ = 0
    for j in range(0,len(class_info)-1):
        if class_info[j] - class_info[j+1] > differ:
            differ = class_info[j] - class_info[j+1]
        else:
            pass
    print(f"Class {i+1}")
    print(f"Max {max(class_info)}, Min {min(class_info)}, Largest gap {differ}")