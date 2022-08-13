char = int(input(),16)

for i in range(1,16):
    print('%X'%char,'*','%X'%i,'=','%X'%(char*i),sep='')