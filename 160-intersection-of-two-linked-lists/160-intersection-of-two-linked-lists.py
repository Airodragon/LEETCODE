# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        StackA = set()
        m = headA
        while m:
            StackA.add(m)
            m = m.next
        n = headB
        while n:
            if n in StackA:
                return n
            n = n.next
        return None