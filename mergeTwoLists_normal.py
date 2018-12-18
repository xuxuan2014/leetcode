# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#this method did not contain recursion, and will exceed the time limit
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        returnList=ListNode(0)
        l=returnList
        
        while l1!=None and l2!=None:
        	if l1.val<l2.val:
        		returnList.next=l1
        		l1=l1.next
        	else:
        		returnList.next=l2
        		l2=l2.next
        	returnList=returnList.next
        if l2:
            returnList.next=l2
        elif l1:
        	returnList.next=l1
        return l.next