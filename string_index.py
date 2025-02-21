import os
os.system("cls")
# s='python'
# s='hello world'
# print(s)
# n="".join(sorted(s))
# print(n)    
def print_by_index(ls,item):
    try:
        print(ls[item])
    except IndexError:
        print("Xatolik mavjud")
    finally:
        print("Xatolik mavjud emas")
ls=[1,5,6,6,8,9,33,44,66,66]
print_by_index(ls,int(input(">> ")))