T = int(input())

for tc in range(1, T+1):
    binary_number = int(input(),2)
    third_number = int(input())
    print(binary_number)
    bin_length = len(str(binary_number))
    thi_length = len(str(third_number))
    
    bin_list = [0]*bin_length
    for i in range(bin_length):
        bin_list[i] = binary_number ^ (i<<i)
    print(bin_list)