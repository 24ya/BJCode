#2108-통계학
import sys
input=sys.stdin.readline
N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))
A.sort()
print1=sum(A)/len(A)
if print1<0:
    if print1-int(print1)<=-0.5:
        print1=int(print1)-1
    else:
        print1=int(print1)
else:
    if print1-int(print1)>=0.5:
        print1=int(print1)+1
    else:
        print1=int(print1)
print2=A[(len(A)//2)]
print4=A[-1]-A[0]
A.reverse()
MAX=0
count=1
print3=A[0]
tmpo=None
for i in range(len(A)):
    if A[i]!=A[i-1]:
        if MAX<count:
            tmpo=None
            print3=A[i-1]
            MAX=count
        elif MAX==count:
            tmpo=print3
            print3=A[i-1]
        count=1
    else:
        count+=1

if MAX<count:
    tmpo=None
    print3=A[-1]
    MAX=count
elif MAX==count:
    tmpo=print3
    print3=A[-1]

if tmpo!=None:
    print3=tmpo

print(print1,print2,print3,print4,sep="\n")