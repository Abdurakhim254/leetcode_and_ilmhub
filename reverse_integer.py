import os
os.system("cls")
def reverse(x):
    if -2147483648<=x<=2147483647:
        if x>0:
            x=int(str(x)[::-1])
            return x
        x=x*-1
        x=int(str(x)[::-1])
        return -1*x
    return 0
n=int(input(" N = "))
print(reverse(n))