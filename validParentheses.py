class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        elif len(s)%2==1:
            return False
        
        d={'{':'}', '[':']', '(':')'}
        stack=[]
        for i in s:
        	if i in d:
        		stack.append(i)
        	else:
        		if stack==[] or d[stack.pop()] != i:
        			return False
        return stack==[]