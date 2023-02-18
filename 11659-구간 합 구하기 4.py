#11659 - 구간합 구하기 4
N,M=map(int,input().split())
A=tuple(map(int,input().split()))
for i in range(M):
    s,f=map(int,input().split())
    s-=1
    total=0
    for j in range(s,f):
        total+=A[j]
    print(total)