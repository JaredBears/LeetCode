class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # addTwoNumbers is solved in O(n) time and O(n) space.  The idea is to iterate through both lists,
    # adding the values of the nodes at the same position together with the carry
    # We find both the value and the carry using the divmod function.  We then create a new node with
    # the value and add it to the list.  We then move to the next node in both lists and repeat the
    # process until we have reached the end of both lists and there is no carry.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, val = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

