class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while i < len(nums):
            if nums[i]==val:
                nums.remove(nums[i])
            else:
                i=i+1
        return len(nums)