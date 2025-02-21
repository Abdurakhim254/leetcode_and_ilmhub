import os
os.system("cls")
def function(nums1,nums2):
    nums1.extend(nums2)
    nums1.sort()
    n=len(ls1)
    if n%2==0:
        median=(nums1[n//2-1]+nums1[n//2])/2
        return median
    else:
        median=nums1[n//2]
        return median
ls1=[1,3]
ls2=[2]
print(function(ls1,ls2))
ls1=[1,2]
ls2=[3,4]
print(function(ls1,ls2))