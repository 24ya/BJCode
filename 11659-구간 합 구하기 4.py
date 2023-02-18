#11659 - 구간합 구하기 4
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=list(map(int,input().split()))
garage=[0]*N
for i in range(N):
    garage[i]=garage[i-1]+A[i]

for i in range(M):
    S, F = map(int, input().split())
    S-=2
    F-=1
    if S<0:
        print(garage[F])
    else:
        print(garage[F]-garage[S])