class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSum=nums[0]
        i=0
        while i<len(nums):
        	temp=0
        	for j in range(i,len(nums)):
        		temp=temp+nums[j]
        		if maxSum<temp:
        			maxSum=temp
        	i=i+1
        return maxSum