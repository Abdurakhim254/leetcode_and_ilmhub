import os
os.system("cls")
def remove_item(nums,val):
    k=0
    for x in range(len(nums)):
        if nums[x]!=val:
            nums[k]=nums[x]
            k+=1
    return k

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_item(nums,val))