# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current=head
        last= None
        while current != None:
           nex=current.next
           current.next=last
           last=current
           current=nex
        self.head=last
        return last
