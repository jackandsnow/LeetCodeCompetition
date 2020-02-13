"""
23. 合并K个排序链表

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def ordered_insert(lists, elem):
    """
    将 elem 有序插入到 lists 中，并返回插入后的有序列表
    """
    if not lists:
        return [elem]

    for i in range(len(lists)):
        # 寻找合适的位置插入
        if lists[i] > elem:
            lists.insert(i, elem)
            break
        # 找不到则插入到末尾
        if i == len(lists) - 1:
            lists.append(elem)
    return lists


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    result = []
    # 遍历每个链表中的元素，将其插入到 result 列表中
    for lt in lists:
        while lt:
            result = ordered_insert(result, lt.val)
            lt = lt.next
    head = ListNode(0)
    temp = head
    # 将有序的列表转换为有序的链表
    for r in result:
        temp.next = ListNode(r)
        temp = temp.next
    return head.next


if __name__ == '__main__':
    ans = ordered_insert([1, 3, 4, 6], 8)
    print(ans)
