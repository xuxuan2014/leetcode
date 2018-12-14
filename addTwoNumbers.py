# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1,temp2=l1,l2
        t=0 #carrier
        
        ans=temp1.val+temp2.val
        t=ans//10
        ans=ans%10
        res=ListNode(ans)
        
        temp3=res
        
        while temp1.next !=None and temp2.next!=None:
            temp1,temp2=temp1.next,temp2.next
            ans=temp1.val+temp2.val+t
            t=ans//10
            ans=ans%10
            temp3.next=ListNode(ans)
            temp3=temp3.next
          
        if temp1.next ==None: temp1=temp2
        while temp1.next != None:
            temp1=temp1.next
            ans=temp1.val+t
            t=ans//10
            ans=ans%10
            temp3.next=ListNode(ans)
            temp3=temp3.next
        
        if t>0:
            temp3.next=ListNode(t)
        
        return res