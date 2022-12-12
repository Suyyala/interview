# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Given two non-empty linked lists representing two non-negative integers,
    add the two numbers and return the sum as a linked list.
    
    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    head = ListNode(0)
    curr = head
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = x + y + carry
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry > 0:
        curr.next = ListNode(carry)
    return head.next
