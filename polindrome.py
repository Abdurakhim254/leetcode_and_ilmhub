import os
os.system("cls")
def polindrome(s):
    n=0
    copy=s
    if s>0:
        while s:
            n=n*10+s%10
            s=s//10
        if copy==n:
            return True
        else:
            return False
    elif s==0:
        return True
    else:
        return False

s=121
# s=10
print(polindrome(s))
# print(s==int(str(s)[::-1]))