#1620-나는야 포켓몬 마스터 이다솜
import sys
input=sys.stdin.readline
N,Q=map(int,input().split(" "))
A=[]
B=dict()
for i in range(N):
    Pokemon=input().rstrip()
    B[Pokemon]=i+1
    A.append(Pokemon)
for i in range(Q):
    ASK=input().rstrip()
    if ASK[0].isupper() or ASK[-1].isupper():
        print(B[ASK])
    else:
        print(A[int(ASK)-1])