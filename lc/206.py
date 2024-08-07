# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prevNode = None
        currNode = head

        while currNode:
            next = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = next
        
        return prevNode