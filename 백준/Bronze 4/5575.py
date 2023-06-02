A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A[0] = A[0] * 3600
A[1] = A[1] * 60
B[0] = B[0] * 3600
B[1] = B[1] * 60
C[0] = C[0] * 3600
C[1] = C[1] * 60
A[3] = A[3] * 3600
A[4] = A[4] * 60
B[3] = B[3] * 3600
B[4] = B[4] * 60
C[3] = C[3] * 3600
C[4] = C[4] * 60
check_A = sum(A[3:]) - sum(A[:3])
check_B = sum(B[3:]) - sum(B[:3])
check_C = sum(C[3:]) - sum(C[:3])
print(check_A // 3600, check_A % 3600 // 60, check_A % 3600 % 60)
print(check_B // 3600, check_B % 3600 // 60, check_B % 3600 % 60)
print(check_C // 3600, check_C % 3600 // 60, check_C % 3600 % 60)