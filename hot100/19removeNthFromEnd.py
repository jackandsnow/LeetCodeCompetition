"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

    给定一个链表: 1->2->3->4->5, 和 n = 2.

    当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：给定的 n 保证是有效的。

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    total = 1
    curr = head
    while curr.next:
        total += 1
        curr = curr.next

    # 顺数第 m 个节点
    m = total - n + 1
    # 只有一个节点或者要删除的是首节点
    if not head.next or m == 1:
        return head.next

    # 找到要删除节点的前一个节点
    curr = head
    while m - 1 > 1:
        curr = curr.next
        m -= 1

    delete = curr.next
    curr.next = delete.next
    return head
