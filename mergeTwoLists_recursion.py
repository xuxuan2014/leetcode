Solution(object):
	def mergeTwoLists(self, l1, l2): 
		""" 
		:type l1: ListNode
		:type l2: ListNode 
		:rtype: ListNode 
		""" 
		if l1 == None and l2 == None:
			return None
		if l1 == None:
			return l2
		if l2 ==None:
			return l1
		if l1.val<l2.val:
			l1.next=self.mergeTwoLists(l1.next,l2)
			return l1
		else:
			l2.next=self.mergeTwoLists(l2.next,l1)
			return l2