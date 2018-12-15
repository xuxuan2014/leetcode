class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=0   
        if x<0:
            flag=1
        
        reverse=0
        while(x):
            temp=x%10
            reverse=reverse*10+temp
            x=x//10
            
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        else:
            if flag==0:
                return reverse
            else:
                return -reverse

#this version exceeds time limit, must improve