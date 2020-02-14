"""
31. 下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1

"""


def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 2
    # 找到 num[i+1] > nums[i] 的位置
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        # 寻找比 nums[i] 略大的数 nums[j]，并交换位置
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    # 反转 nums[i] 后面的所有数字，以获取它们的最小排列
    l, r = i + 1, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    print(nums)


if __name__ == '__main__':
    nextPermutation([1, 3, 2])
