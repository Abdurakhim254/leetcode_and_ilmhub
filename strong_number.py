import os
os.system("cls")
# def getfactorial(n):
#     fact=1
#     x=1
#     while x<=n:
#         fact=fact*x
#         x+=1
#     return fact
# son=int(input("N = "))
# s=0
# copy=son
# while son:
#     n=son%10
#     s+=getfactorial(n)
#     son=son//10
# if copy==s:
#     print(True)
# else:
#     print(False)
def getfactorial(n):
    fact=1
    x=1
    while x<=n:
        fact=fact*x
        x+=1
    return fact
son=int(input("Son = "))
s=0
i=1
while i<son:
    copy=i
    s=0
    temp=i
    while temp:
        n=temp%10
        s+=getfactorial(n)
        temp=temp//10
    if s==copy:
        print(copy,end=" ")
    i+=1