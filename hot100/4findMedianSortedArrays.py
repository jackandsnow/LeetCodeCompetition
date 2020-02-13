"""
4. 寻找两个有序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

    nums1 = [1, 3]
    nums2 = [2]

    则中位数是 2.0

示例 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    则中位数是 (2 + 3)/2 = 2.5

"""


def get_median(nums_list):
    """
    获取 nums_list 的中位数
    :param nums_list: 数字列表
    :return: float 中位数
    """
    mid = len(nums_list) // 2
    return float(nums_list[mid] + nums_list[mid - 1]) / 2 if len(nums_list) % 2 == 0 else float(nums_list[mid])


def findMedianSortedArrays1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # 二者都不为空
    if nums1 and nums2:
        result = []
        i, j = 0, 0
        # 遍历nums1和nums2，将其中较小的数依次填加到result中
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        # nums1或nums2未遍历完的元素直接加到result末尾
        result.extend(nums1[i:]) if i < len(nums1) else result.extend(nums2[j:])
        return get_median(result)
    # nums1为空
    elif not nums1:
        return get_median(nums2)
    # nums2为空
    else:
        return get_median(nums1)


def findMedianSortedArrays2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if not nums1 and not nums2:
        return float(0)

    # 记录不同数字的个数
    dic = {}
    for n1 in nums1:
        if n1 not in dic:
            dic[n1] = 1
        else:
            dic[n1] += 1
    for n2 in nums2:
        if n2 not in dic:
            dic[n2] = 1
        else:
            dic[n2] += 1

    n = len(nums1) + len(nums2)
    if n % 2 == 0:  # 偶数
        a, b = n // 2, n // 2 + 1
    else:  # 奇数
        a, b = n // 2 + 1, n // 2 + 1
    # 存储有序的不同数字
    keys = list(dic.keys())
    # 所有数相同
    if len(keys) == 1:
        return float(keys[0])
    keys.sort()
    cnt = 0
    for i in range(len(keys) - 1):
        cnt += dic[keys[i]]
        # b <= cnt
        if cnt >= b:
            return float(keys[i])
        # a <= cnt < b
        elif cnt >= a and cnt + dic[keys[i + 1]] >= b:
            return float(keys[i] + keys[i + 1]) / 2


if __name__ == '__main__':
    ans = findMedianSortedArrays2([1, 3], [2])
    print(ans)
