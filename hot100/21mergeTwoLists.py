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


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # l1, l2都为空链表
    if not l1 and not l2:
        return None

    # l1, l2中有非空表
    result = ListNode(0)
    temp = result
    while l1 or l2:
        if l1 and not l2:
            temp.next = l1
            break
        elif not l1 and l2:
            temp.next = l2
            break
        else:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
    return result.next
