#7119-The Magician

b,d,r,p=map(int,input().split())
count=0
while b>=2:
    before=(b,d,r,p)
    if  ((b//2)-3<=min(p,d) or r<1) and b>=2 and d>=1 and p>=1:
        b-=2
        d-=1
        r+=3
        p-=1
        count+=1
        continue

    if (p<((b-4)//2) and p<=d) and b>=4 and d>=2 and r>=1:
        if b<=6 and d<3:
            break
        b-=4
        d-=2
        r-=1
        p+=2
        count+=1
        continue

    if (d < ((b - 1) // 2) and d <= p) and b >= 1 and r >= 1 and p >= 1:
        if b<=3 and p<2:
            break
        b -= 1
        d += 4
        r -= 1
        p -= 1
        count += 1
        continue
    after=(b,d,r,p)

    if (d<1 and p<1) or before==after:
        break
# def finder(d,b,r,p):
#     count=0
#     line=""
#     return max(A(b, d, r, p, count,line), B(b, d, r, p, count,line), C(b, d, r, p, count,line))
#
#
# def A(b,d,r,p,count,line):
#     if b<4 or d<2 or r<1:
#         return (r,-count,line)
#     else:
#         b-=4
#         d-=2
#         r-=1
#         p+=2
#         count+=1
#         line=line+"1"
#         return max(A(b,d,r,p,count,line),B(b,d,r,p,count,line),C(b,d,r,p,count,line))
#
# def B(b,d,r,p,count,line):
#     if b<2 or d<1 or p<1:
#         return (r,-count,line)
#     else:
#         b-=2
#         d-=1
#         r+=3
#         p-=1
#         count+=1
#         line=line+"3"
#         return max(A(b,d,r,p,count,line),B(b,d,r,p,count,line),C(b,d,r,p,count,line))
#
# def C(b,d,r,p,count,line):
#     if b<1 or r<1 or p<1:
#         return (r,-count,line)
#     else:
#         b-=1
#         d+=4
#         r-=1
#         p-=1
#         count+=1
#         line=line+"2"
#         return max(A(b,d,r,p,count,line),B(b,d,r,p,count,line),C(b,d,r,p,count,line))
#
#
# print(finder(d,b,r,p))
print(r,count,sep=" ")