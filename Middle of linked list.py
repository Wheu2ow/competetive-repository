# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        leng=0
        current=head
        while current != None:
            leng+=1
            current=current.next
        pos=0
        temp=head
        while pos<((leng//2)):
            temp=temp.next
            pos+=1
        return temp
