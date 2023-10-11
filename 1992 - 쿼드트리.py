#1992 - 쿼드트리
line=""
N=int(input())
for _ in range(N):
    line+=input()

def tree(line,N):
    if len(line)==1:
        return line
    else:
        l1,l2,l3,l4="","","",""
        temp=0
        for i in range(N//2):
            l1+=line[temp:N//2+temp]
            l2+=line[N//2+temp:N+temp]
            l3+=line[(N**2)//2+temp:(N**2)//2+temp+N//2]
            l4+=line[(N**2)//2+temp+N//2:(N**2)//2+temp+N]
            temp+=N
        r1,r2,r3,r4=tree(l1,N//2),tree(l2,N//2),tree(l3,N//2),tree(l4,N//2)
        if r1==r2 and r2==r3 and r3==r4 and len(r1)==1:
            return r1
        else:
            return "("+r1+r2+r3+r4+")"

print(tree(line,N))