"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    temp = result
    # 记录进位
    bit = 0
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + bit
        bit = total // 10
        temp.next = ListNode(total % 10)
        # 指针继续往后移动
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        temp = temp.next

    # 末尾还存在进位
    if bit != 0:
        temp.next = ListNode(bit)
    return result.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    ans = addTwoNumbers(l1, l2)
    while ans:
        if ans.next:
            print(ans.val, end=' -> ')
        else:
            print(ans.val)
        ans = ans.next
