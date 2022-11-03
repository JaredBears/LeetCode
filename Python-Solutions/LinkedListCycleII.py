# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycleNaive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head
        while curr and curr.next:
            if curr.next in visited:
                return curr.next
            visited.add(curr)
            curr = curr.next

    #better
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def intersect(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
        inter = intersect(head)
        if not inter:
            return
        ptr = head
        while ptr != inter:
            ptr = ptr.next
            inter = inter.next
        return ptr
