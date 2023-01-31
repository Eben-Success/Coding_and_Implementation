class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def sortList(head):
    if not head or not head.next:
        return head

    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)


def merge(left, right):
    dummy = cur = ListNode(0)

    while left and right:
        if left.val < right.val:
            cur.next = left
            left = left.next

        else:
            cur.next = right
            right = right.next
        cur = cur.next

    cur.next = left if left else right

    return dummy.next