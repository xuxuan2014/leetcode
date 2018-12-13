class Solution(object):
	def twoSum(self,nums,target):
		dic={}
		for i, num in enumerate(nums):
			sub=target-num
			if sub in dic:
				return [dic[sub],i]
			else:
				dic[num]=i