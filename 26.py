class Solution(object):
    def removeDuplicates(self, nums):
        length=len(nums)
        i=0
        for j in range (i+1,length):
            if (nums[i]!=nums[j]):
                i=i+1
                nums[i]=nums[j]
        return i+1