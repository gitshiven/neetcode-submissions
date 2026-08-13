# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr and count<k:
            curr = curr.next
            count+=1
        if count<k:
            return head
        
        prev = None
        curr = head # reset
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        #merge
        head.next = self.reverseKGroup(curr,k)
        return prev      