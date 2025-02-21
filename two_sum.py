import os
os.system("cls")
def function(nums,target):
    res=[]
    for x in range(len(nums)-1):
        for y in range(x+1,len(nums)):
            if nums[x]+nums[y]==target:
                res.append(x)
                res.append(y)
    return list(set(res))
nums = [2,7,11,15]
target = 9
print(function(nums,target))
nums=[3,2,4]
target=6
print(function(nums,target))
nums=[3,2,3]
target=6
print(function(nums,target))
nums=[2,5,5,11]
target=10
print(function(nums,target))
nums=[-1,-2,-3,-4,-5]
target=-8
print(function(nums,target))