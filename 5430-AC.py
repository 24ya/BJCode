#5430-AC
import sys
input=sys.stdin.readline
N=int(input()) #시행 횟수
for _ in range(N):
    command=input().rstrip() #readline으로 받으면 줄바꿈문자 포함되므로 rstrip
    elem_amount=int(input())
    elem=eval(input())
    D_count=command.count("D")
    if D_count>elem_amount: #D가 더 많으면 error 출력
        print("error")
        continue
    elif D_count==elem_amount: #D 갯수가 같으면 빈 리스트 출력
        print("[]")
        continue
    R_count=0 #D가 나오는 앞까지 리버스 횟수 저장
    start,end=0,len(elem)
    front_back=True #원래 처음 리스트 순서인지 확인하는 변수

    for i in range(len(command)):
        if command[i]=="D": #D 명령어를 R(Pop)R로 생각
            R_count+=1
            if R_count%2!=0:
                front_back=not front_back
            if front_back==True: #처음 순서와 같을 경우 뒤에 pop
                end-=1
            else: #뒤집힌 순서일 경우 앞에 pop
                start+=1
            R_count=1
        else:
            R_count+=1
    elem=elem[start:end]
    if R_count%2==1: #리버스 횟수가 남았을 경우
        front_back=not front_back
    if front_back!=True:
        elem.reverse()

    #출력부
    if len(elem)>0:
        print("[",end='')
        for i in range(len(elem)-1):
            print(elem[i],end=',')
        print("%d]"%(elem[-1]))
    else:
        print("[]")