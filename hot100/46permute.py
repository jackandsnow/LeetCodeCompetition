"""
46. 全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

"""


def permute(nums):
    """
    字典序排列算法
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 排好序，便于进行字典序排列
    nums.sort()
    result = [nums[:]]
    n = len(nums)
    i = n - 1
    while i > 0:
        # 找到 nums[i-1] < nums[i]的位置
        if nums[i - 1] < nums[i]:
            # 找到比 nums[i-1] 略大的数 nums[j]
            j = n - 1
            while j > i and nums[j] <= nums[i - 1]:
                j -= 1
            # 交换 nums[i-1] 和 nums[j]
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            # nums[i:] 后续升序排列
            l, r = i, n - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            result.append(nums[:])
            # 重置 i，寻找下一个排列
            i = n - 1
        else:
            i -= 1
    return result


if __name__ == '__main__':
    ans = permute([1, 2, 4, 3])
    print(ans)
