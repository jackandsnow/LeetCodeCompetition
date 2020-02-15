"""
33. 搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4

示例 2:

    输入: nums = [4,5,6,7,0,1,2], target = 3
    输出: -1

"""


def search(nums, target):
    """
    二分查找法
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # 左，右 指针
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        # 找到目标值
        if nums[m] == target:
            return m
        # 正常序
        if nums[l] < nums[r]:
            # 右移
            if nums[m] < target:
                l = m + 1
            # 左移
            else:
                r = m - 1
        # 旋转序
        else:
            if nums[m] < target:
                # 右侧有序小于 target，左移
                if nums[m] <= nums[r] < target:
                    r = m - 1
                # 右移
                else:
                    l = m + 1
            else:
                # 左侧有序大于 target，右移
                if nums[m] >= nums[l] > target:
                    l = m + 1
                # 左移
                else:
                    r = m - 1
    return -1


if __name__ == '__main__':
    ans = search([6, 2, 3, 4, 5], 2)
    print(ans)
