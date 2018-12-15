class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        r=str(x)[::-1]
        r=int(r)
        if r==x:
            return True
        else:
            return False