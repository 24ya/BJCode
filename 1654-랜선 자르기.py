#1654 - 랜선 자르기
N,K=map(int,input().split())
LAN=[]
for _ in range(N): LAN.append(int(input()))
M,start,end=max(LAN),1,max(LAN)
while start<=end:
    total=0
    mid=(start+end)//2
    for i in LAN:
        total+=i//mid
    if total>=K: start=mid+1
    else: end=mid-1
print(start-1)