import os
os.system("cls")
ls1=[2,4,3]
ls2=[5,6,4]
ls1.reverse()
ls2.reverse()
res=''
for x in ls1:
    res+=str(x)
res+='+'
for x in ls2:
    res+=str(x)
print(res)
s=eval(res)
s=str(s)
ls3=[]
print(type(s))
for x in s:
    ls3.append(int(x))
ls3.reverse()
print(ls3)