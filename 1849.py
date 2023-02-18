#1849-순열
import sys
input=sys.stdin.readline
class Node:
    def __init__(self,e):
        self.data=e
        self.link=None
class MyList:
    def __init__(self):
        self.head=None
    def getNode(self,pos):
        if pos<0: return None
        node=self.head
        while pos>0 and node!=None:
            node=node.link
            pos-=1
        return node
    def insertion(self,pos,elem):
        node=Node(elem)
        before=self.getNode(pos-1)
        if before==None:
            node.link=self.head
            self.head=node
        else:
            node.link=before.link
            before.link=node
    def print(self):
        node=self.head
        while node!=None:
            print(node.data)
            node=node.link

A=MyList()
B=[]
N=int(input())
for _ in range(N):
    B.append(int(input()))
count=N
for i in range(N):
    A.insertion(B.pop(),count)
    count-=1
A.print()