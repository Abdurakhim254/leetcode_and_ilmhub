import os
os.system("cls")
def remove_item(ls,item):
    for x in range(len(ls)):
        if ls[x]==item:
            ls[x]='_'
    for x in range(len(ls)):
        for y in range(len(ls)-1):
            if ls[y]=='_' and str(ls[y+1]) in '0123456789':
                ls[y],ls[y+1]=ls[y+1],ls[y]
    return ls
# ls=list(map(int,input("List elementlarini kiriting : ").split()))
# print(ls)
# item=int(input("O'chirmoqchi bolgan elementni kiriting : "))
# print(remove_item(ls,item))
nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_item(nums,val))