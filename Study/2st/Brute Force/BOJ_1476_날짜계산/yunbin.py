E, S, M = map(int,input().split())

result = 0 

A,B,C = 0,0,0 


while True:

    if A == E and B ==S and C==M :
        break;
    result += 1

    A+= 1
    B += 1
    C += 1

    if A >15:
        A= 1
    if B >28:
        B= 1

    if C > 19:
        C =1
print(result)