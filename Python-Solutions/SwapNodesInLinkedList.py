class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # This is solved in O(n) time and O(1) space. The idea is to use two pointers
    # to find the nodes at the kth and n-k+1th positions. Then, we swap the values
    # of the nodes.
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        i = 1
        while i < k and fast and fast.next:
            fast = fast.next
            i += 1
        temp = fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.val, temp.val = temp.val, slow.val
        return head