T = input()
waiting = 0
time_dict={}

num_dict={
    1:"",
    2:"A,B,C",
    3:"D,E,F",
    4:"G,H,I",
    5:"J,K,L",
    6:"M,N,O",
    7:"P,Q,R,S",
    8:"T,U,V",
    9:"W,X,Y,Z",
    0:""
}

for i in range(1,11):
    time_dict[i%10] = 1+i

for j in T:
    for k,v in num_dict.items():
        if j in v:
            waiting+=time_dict[k]
print(waiting)