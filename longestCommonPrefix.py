class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        elif len(strs)==1:
            return strs[0]

        j=0
        minlength=min([len(x) for x in strs])
        while j<minlength:
        	for i in range(1,len(strs)):
        		if strs[0][j]!=strs[i][j]:
        			if j==0:
        				return ""
        			else:
        				return strs[0][:j]
        	j=j+1
        return strs[0][:j]