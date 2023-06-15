N = int(input())

middle_value = 0
left = 0
right = N
r_check = 0
l_check = 0
middle = N/2
answer = 0

for _ in range(3):
    A,B = map(int,input().split())
    if middle_value == 0:
        check = (A+B)/2
        if check < middle:
            left = N-check
            l_check = 1
        elif check > middle:
            right = check
            r_check = 1
        else:
            answer = middle
            r_check = 1
            l_check = 1
        middle = (right+left)/2
    else:
        if r_check == 1:
            if A >= right and B >= right:
                pass
            elif max(A,B) >= right and min(A,B) <= right:
                check = (min(A,B)+(max(A,B)-(max(A,B)-right)))/2
                if check < middle:
                    left = right-check
                    l_check = 1
                    r_check = 0
                elif check > middle:
                    right = check
                    r_check = 1
                    l_check = 0
                else:
                    answer = middle
                    r_check = 1
                    l_check = 1
                middle = (right+left)/2
            else:
                check = (A+B)/2
                if check < middle:
                    left = right-check
                    l_check = 1
                    r_check = 0
                elif check > middle:
                    right = check
                    r_check = 1
                    l_check = 0
                else:
                    answer = middle
                    r_check = 1
                    l_check = 1
                middle = (right+left)/2
        elif l_check == 1:
        
        else:


print(f"{answer:.1f}")