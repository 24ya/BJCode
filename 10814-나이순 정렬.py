#10814 - 나이순 정렬
n=int(input(""))
age=[]
name=[]
sort_age=[]
for i in range(n):
    line=input().split(' ')
    age.append(int(line[0]))
    name.append(line[1])
sort_age=sorted(list(set(age)))
for i in sort_age:
    for j in range(len(age)):
        if age[j]==i:
            print(i,end=' ')
            print(name[j])