class Solution:
    def removeDuplicates(self, nums):
        return list(set(nums))[1]


mn=Solution()
ls=[1,1,2]
print(mn.removeDuplicates(ls))