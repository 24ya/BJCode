#2805-나무 자르기
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
start,end=0,A[0]
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in range(len(A)):
        if A[i]>mid:
            cnt+=A[i]-mid
        else:
            break
    if cnt>=m:
        start=mid+1
    else:
        end=mid-1
print(start-1)
#pypy