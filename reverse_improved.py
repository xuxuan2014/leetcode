class Solution(object):
	def reverse(self, x):
		flag=1
		if x<0:
			flag=-1
			x=-x
		R=str(x)[::-1]
		R=int(R)
		if R<-2**31 or R>2**31-1:
            return 0
        else:
            return flag*R
