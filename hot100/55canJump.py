"""
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

    输入: [2,3,1,1,4]
    输出: true
    解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:

    输入: [3,2,1,0,4]
    输出: false
    解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

"""


def canJump1(nums):
    """
    动态规划算法
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    # 标记能否跳到终点位置，0-不能，1-能
    flag = [0] * n
    flag[n - 1] = 1
    # 从右往左寻找能跳到终点的所有点
    for i in range(n - 2, -1, -1):
        further_jump = min(i + nums[i], n - 1)
        for j in range(i + 1, further_jump + 1):
            if flag[j] == 1:
                flag[i] = 1
                break
    # 最终看起点是否也能跳到
    return flag[0] == 1


def canJump2(nums):
    """
    贪心算法
    :type nums: List[int]
    :rtype: bool
    """
    last_pos = len(nums) - 1
    # 从右向左迭代，对每个节点检查是否存在一步跳跃可以到达最后一个位置
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last_pos:
            last_pos = i
    return last_pos == 0


if __name__ == '__main__':
    ans = canJump2([2, 0, 2, 0])
    print(ans)
