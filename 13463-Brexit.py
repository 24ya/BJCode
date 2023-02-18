import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
class country:
    def __init__(self,n):
        self.name=n
        self.friend=[]
        self.limit=0
        self.inGroup=True
    def plusfriend(self,e):
        self.friend.append(e)
    def delfriend(self,e):
        if self.inGroup==True:
            self.friend.remove(e)
    def checkExit(self):
        if len(self.friend)<=self.limit:
            self.exitGroup()
    def setlimit(self):
        self.limit=len(self.friend)/2
    def exitGroup(self):
        self.inGroup=False
        for i in self.friend:
            c_list[i-1].delfriend(self.name)
    def getStatus(self):
        if self.inGroup==True:
            return "stay"
        return "leave"



C,P,X,L=map(int,input().split())
c_list=[]
for i in range(C):
    c_list.append(country(i+1))
for _ in range(P):
    c1,c2=map(int,input().split())
    c_list[c1-1].plusfriend(c2)
    c_list[c2-1].plusfriend(c1)
for i in range(C):
    c_list[i].setlimit()
c_list[L-1].exitGroup()
different=True
while different==True:
    different=False
    for i in range(C):
        before=c_list[i].getStatus()
        if before=="stay":
            c_list[i].checkExit()
            after=c_list[i].getStatus()
            if before!=after:
                different=True
        if c_list[X-1].getStatus()=="leave":
            break
    if c_list[X-1].getStatus() == "leave":
        break
print(c_list[X-1].getStatus())