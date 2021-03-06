"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

"""


def violent_method(nums, target):
    """
    暴力法，两重循环搜索解
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def hash_method(nums, target):
    """
    利用字典实现 Hash表
    """
    # 转换为 (value, id) 字典
    dic = dict(map(lambda x: (x[1], x[0]), enumerate(nums)))

    for i, v in enumerate(nums):
        j = dic.get(target - v)
        # 找到 target-v 且不是本身
        if j and i != j:
            return [i, j]


def twoSum(nums, target):
    # violent_method(nums, target)
    hash_method(nums, target)


if __name__ == '__main__':
    ans = twoSum([2, 7, 5, 11, 15], 9)
    print(ans)
