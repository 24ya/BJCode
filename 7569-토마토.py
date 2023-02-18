#7576-토마토
LIST=[]
M,N=map(int,input().split())
for i in range(N):
    LIST.append(list(map(int,input().split())))

def Check(LIST):
    for i in range(len(LIST)):
        for j in range(len(LIST[i])):
            if LIST[i][j]==0:
                return 0
    return 1

def Tomato(x,y):
    global LIST
    if LIST[x][y]==0:
        LIST[x][y]=1
