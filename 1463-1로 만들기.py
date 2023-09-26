#1463-1로 만들기

N=int(input())
DP=[None]*(N+1)
DP[1]=0


for i in range(2,N+1):
    before=DP[i-1]
    if i%3==0:
        before=min(before,DP[i//3])
    if i%2==0:
        before=min(before,DP[i//2])
    DP[i]=before+1

print(DP[N])