# You are given the head of a linked list. Delete the middle node, and return
# the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start
# using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or
# equal to x.
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2,
# respectively.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    def helper(head):
        if not head:
            return
        if head.next:
            return str(head.val) + ", " + helper(head.next)
        return str(head.val)
    if head:
        print("[" + helper(head) + "]")
    else:
        print("[]")

def deleteMiddle(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head == None or head.next == None:
        return head
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

printList(deleteMiddle(list))
