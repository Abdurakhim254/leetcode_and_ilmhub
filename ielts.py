import os
os.system("cls")
def get_score(a,b,c,d):
    n=(a+b+c+d)/4
    return n
def get_round(n):
    pass

a,b,c,d=map(float,input().split())
print(get_score(a,b,c,d))