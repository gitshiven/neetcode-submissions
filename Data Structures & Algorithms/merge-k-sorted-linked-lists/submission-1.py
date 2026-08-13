# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        normal_list = []
        for node in lists:
            curr = node
            while curr:
                normal_list.append(curr.val)
                curr = curr.next
        
        normal_list.sort() #sort kardi List

        #linked list banao

        dummy = ListNode(0)
        curr = dummy

        for val in normal_list:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next