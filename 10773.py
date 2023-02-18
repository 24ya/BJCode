#10773-제로

N=int(input())
A=[]
for i in range(N):
    a=int(input())
    if a==0:
        A.pop()
    else:
        A.append(a)
print(sum(A))