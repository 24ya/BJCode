#2805-나무 자르기
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=list(map(int,input().split()))
start,end=0,max(A)
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in A:
        if i>mid:
            cnt+=i-mid
    if cnt>=m:
        start=mid+1
    else:
        end=mid-1
print(start-1)