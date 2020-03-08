"""
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

    输入: nums = [1,2,3]
    输出:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

"""


def subsets(nums):
    """
    递归法
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 初始子集为空
    result = [[]]
    # 每一步向子集添加新的整数，并生成新的子集
    for num in nums:
        result += [res + [num] for res in result]
    return result


if __name__ == '__main__':
    ans = subsets([1, 2, 3])
    print(ans)
