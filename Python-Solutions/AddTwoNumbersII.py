class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # addTwoNumbers is solved in O(n) time and O(n) space. The idea is to add the
    # two lists together and then fix the list. We add the two lists together by
    # adding the values of the nodes at the same position. 
    # We fix the list by iterating through the list and adding the values of the
    # nodes that are greater than 10 to the previous node. We do this recursively
    # until we don't have to make any changes to the list.

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addLists(head1, head2, k):
            dummy = ListNode(0)
            curr = dummy
            for i in range(k):
                curr.next = ListNode(head1.val)
                head1 = head1.next
                curr = curr.next
            while head1 and head2:
                curr.next = ListNode(head1.val + head2.val)
                curr = curr.next
                head1 = head1.next
                head2 = head2.next
            return fixList(dummy)
        def fixList(dummy):
            curr = dummy.next
            prev = dummy
            changes = 0
            while curr:
                if curr.val >= 10:
                    prev.val += 1
                    changes += 1
                    curr.val -= 10
                prev = curr
                curr = curr.next
            if changes > 0:
                return fixList(dummy)
            if dummy.val > 0:
                return dummy
            return dummy.next
        n1 = 0
        n2 = 0
        curr1 = l1
        curr2 = l2
        while curr1 or curr2:
            if curr1:
                n1 += 1
                curr1 = curr1.next
            if curr2:
                n2 += 1
                curr2 = curr2.next
        if n1 > n2:
            return addLists(l1, l2, n1-n2)
        else:
            return addLists(l2, l1, n2-n1)