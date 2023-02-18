import sys
input=sys.stdin.readline

class Node(e):
    def __init__(self):
        self.e=e
        self.before=None
        self.next=None


N=int(input())
for _ in range(N):
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=[]
    for i in range(n):
        B.append((A[i],i))
    find=B[m-1]
    B.sort()
    print(B.index(find)+1)