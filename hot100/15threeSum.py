"""
15. 三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

    给定数组 nums = [-1, 0, 1, 2, -1, -4]，

    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 元素少于3个，返回空列表
    if len(nums) < 3:
        return []
    nums.sort()
    result = []
    for i in range(len(nums)):
        # num[i] > 0 后不会存在3个数和为0
        if nums[i] <= 0:
            # 去重 nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # 去重 num[l] 和 nums[r]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # 两指针向中间移动
                    l += 1
                    r -= 1
    return result


if __name__ == '__main__':
    ans = threeSum(
        [-1, 0, 1, 2, -1, -4]
    )
    print(ans)
