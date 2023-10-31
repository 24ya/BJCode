#1074 - Z

def Z(N,x,y):
    if N<0:
        return 0
    div=2**(N-1)
    if div>x and div>y:  #1번구역
        return Z(N-1,x,y)
    elif div>x and div<=y: #2번구역
        return Z(N-1,x,y-div)+(2**(2*N-2))
    elif div<=x and div>y: #3번구역
        return Z(N-1,x-div,y)+(2**(2*N-1))
    else: #4번구역
        return Z(N-1,x-div,y-div)+(2**(2*N-2))*3

N,r,c=map(int,input().split())
print(Z(N,r,c))