class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1,len(nums)):
            res=max(nums[i-1]+nums[i],nums[i])
            nums[i]=res
        return max(nums]