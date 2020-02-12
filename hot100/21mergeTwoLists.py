"""
21. 合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists1(l1, l2):
    """
    迭代法，28ms
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # l1, l2均为非空链表
    result = ListNode(0)
    temp = result
    while l1 and l2:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    # l1, l2存在空链表
    temp.next = l1 if l1 else l2
    return result.next


def mergeTwoLists2(l1, l2):
    """
    迭代法，16ms
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # l1, l2都为空链表
    if not l1 and not l2:
        return None

    result = ListNode(0)
    temp = result
    while l1 or l2:
        # 直接加 l1
        if l1 and not l2:
            temp.next = l1
            break
        # 直接加 l2
        elif not l1 and l2:
            temp.next = l2
            break
        # 加 l1 和 l2 中较小的数
        else:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
    return result.next
