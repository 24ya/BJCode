#2606 - 바이러스

Graph={}
queue=[1]
done=[]
N=int(input())
for _ in range(int(input())):
    first,second=map(int,input().split())
    if first in Graph.keys():
        Graph[first].append(second)
    else:
        Graph[first]=[second]
    if second in Graph.keys():
        Graph[second].append(first)
    else:
        Graph[second]=[first]
    

while len(queue)>0:
    n=queue.pop(0)
    if n in done:
        continue
    done.append(n)
    if n in Graph.keys():
        queue.extend(Graph[n])
print(len(done)-1)