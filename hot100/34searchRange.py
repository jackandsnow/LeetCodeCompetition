"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]

示例 2:

    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]

"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 查找左边界（右边界）
    def next_bound(left_flag):
        # 搜索闭区间 [l, r]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            # 向左侧收缩
            if nums[m] > target or (left_flag and nums[m] == target):
                r = m - 1
            # 向右侧收缩
            else:
                l = m + 1
        return l

    # 查找左边界
    left = next_bound(True)
    # 没有找到 target
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    # 查找右边界返回的 l = r + 1，故右侧需减 1
    return [left, next_bound(False) - 1]


if __name__ == '__main__':
    ans = searchRange([5, 6, 7, 8, 10], 7)
    print(ans)
