class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        repeat=0
        initialLength=len(nums)
        while i+1 < len(nums):
        	if nums[i]==nums[i+1]:
        		repeat=repeat+1
        		nums.remove(nums[i+1])
        	else:
        		i=i+1
        count=initialLength-repeat
        #print count
        return count