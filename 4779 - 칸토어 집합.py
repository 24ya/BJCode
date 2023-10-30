#4779 - 칸토어 집합
import sys
def cantor(line):
    length=len(line)
    if length<=1:
        return line
    new_line="-"*(length//3)+" "*(length//3)+"-"*(length//3)
    return cantor(new_line[:length//3])+" "*(length//3)+cantor(new_line[length*2//3:])

while True:
    N=sys.stdin.readline().rstrip()
    if N=="":
        break
    N=int(N)
    line="-"*3**N
    print(cantor(line))