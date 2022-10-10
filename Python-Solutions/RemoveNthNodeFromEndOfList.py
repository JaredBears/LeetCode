# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.
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

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    sentinal = ListNode(0, head)
    slow = fast = sentinal
    i = 0
    while fast:
        if i > n:
            slow = slow.next
        fast = fast.next
        i += 1
    if slow.next:
        slow.next = slow.next.next
    else:
        return head.next
    return sentinal.next

testListOne = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
testListTwo = ListNode(1)
testListThree = ListNode(1, ListNode(2))
testListFour = ListNode(1, ListNode(2))

printList(removeNthFromEnd(testListOne, 2))
printList(removeNthFromEnd(testListTwo, 1))
printList(removeNthFromEnd(testListThree, 1))
printList(removeNthFromEnd(testListFour, 2))
