class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[len(nums)-1]<target:
            nums.append(target)
        for i in range(0,len(nums)):
            if nums[i]>=target:
                nums.insert(i,target)
                return i