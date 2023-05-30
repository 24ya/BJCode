#1316 - 그룹 단어 체커
N=int(input())
count=0
for _ in range(N):
    word=input()
    W=word[0]
    A=[]
    for i in word:
        if i!=W:
            A.append(W)
        W=i
    A.append(word[-1])
    if len(set(A))==len(A):
        count+=1
print(count)