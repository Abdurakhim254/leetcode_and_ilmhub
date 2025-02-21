import os
os.system("cls")
# def max_polindrome(max):
#      if max==max[::-1]:
#          return max
def max_string(res):
    max=[]
    for x in range(len(res)):
        if len(max)<len(res[x]):
            max=res[x]
    # return max_polindrome(max)
    return len(max)
def function(s):
    res=[]
    kerak=''
    for x in range(len(s)-1):
        if s[x]!=s[x+1]:
            kerak+=s[x]
        else:
            res.append(kerak+s[x])
            kerak=''
    kerak+=s[-1]
    res.append(kerak)
    for x in range(len(res)):
        res[x]=list(set(res[x]))
    # return res
    return max_string(res)

s=input("Matn yoki satr kiriting : ")
print(function(s))