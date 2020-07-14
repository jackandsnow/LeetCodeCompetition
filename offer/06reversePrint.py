"""
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

    输入：head = [1,3,2]
    输出：[2,3,1]

限制：
    0 <= 链表长度 <= 10000
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reversePrint(head):
    """
    :param head: ListNode
    :return: List[int]
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    result.reverse()
    return result


if __name__ == '__main__':
    begin = ListNode(1)
    begin.next = ListNode(3)
    begin.next.next = ListNode(2)
    ans = reversePrint(begin)
    print(ans)
