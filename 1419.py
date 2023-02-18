#1419-등차수열의 합

l=int(input())
r=int(input())
k=int(input())

def Find1419(l,r,k):
    if k==2:
        if l>2:return r-l+1
        else:
            if r<3: return 0
            else: return r-2
    elif k==3:
        # x+(x+d)+(x+2d)=3(x+d)
        if l%3==0: l=l//3
        else: l=(l//3)+1
        r=r//3
        if l>1:return r-l+1
        else:
            if r<2: return 0
            else: return r-1

    elif k==4:
        # x+(x+d)+(x+2d)+(x+3d)=4x+6d=2(2x+3d) 5 7 8 9 10
        if l%2==0: l=l//2
        else: l=(l//2)+1
        r=r//2
        if l>6: return r-l+1
        else:
            if r<5:return 0
            else:
                if l==6: return r-6
                if r<7: return 1
                return r-5

    elif k==5:
        # x+(x+d)+(x+2d)+(x+3d)+(x+4d)=5(x+2d)
        if l%5==0: l=l//5
        else: l=(l//5)+1
        r=r//5
        if l>2: return r-l+1
        else:
            if r<3: return 0
            else: return r-2

print(Find1419(l,r,k))