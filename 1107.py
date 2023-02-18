#1107-리모컨
import sys
input=sys.stdin.readline

channel=int(input())
errorAmount=int(input())
errorList=input().split()
just=abs(channel-100)
count=just
for i in range(1000000):
    num=str(i)
    for j in range(len(num)):
        if num[j] in errorList:
            break
        elif j==(len(num)-1):
            count=min(count,abs(channel-i)+len(num))
print(count)