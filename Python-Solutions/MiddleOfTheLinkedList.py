# Given the head of a singly linked list, return the middle node of the linked
# list.
#
# If there are two middle nodes, return the second middle node.
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


def middleNodeNaive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    curr = head;
    count = 0
    while curr:
        count += 1
        curr = curr.next

    mid = (count // 2)

    count = 0
    curr = head
    while curr:
        if(count == mid):
            return curr
        count += 1
        curr = curr.next

    return head

#Better
def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

testOne = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
testTwo = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))

printList(middleNode(testOne))
printList(middleNode(testTwo))
