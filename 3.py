class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        start=0
        end=0
        length=len(s)
        dic={}
        for end in range(0,length):
            if s[end] in dic:
                start=max(start, dic[s[end]]+1)
            dic[s[end]]=end
            res=max(res, end-start+1)
        return res