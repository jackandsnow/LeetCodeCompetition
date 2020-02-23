"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""


def maxSubArray1(nums):
    """
    动态规划方法
    :type nums: List[int]
    :rtype: int
    """
    # 保存当前最大和，最终结果
    curr_sum, result = 0, nums[0]
    for num in nums:
        # 对结果有增益价值，则继续加和
        if curr_sum > 0:
            curr_sum += num
        # 无增益价值，则更换为当前数字
        else:
            curr_sum = num
        # 更新当前获得的结果
        result = max(result, curr_sum)
    return result


def maxSubArray2(nums):
    """
    分治法
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    # 左半边的最大子序和
    maxleft = maxSubArray2(nums[:n // 2])
    # 右半边的最大子序和
    maxright = maxSubArray2(nums[n // 2:])
    # 中间的最大子序和
    m = n // 2
    templ, tempr = 0, 0
    mid_maxl, mid_maxr = nums[m - 1], nums[m]
    for i in range(m):
        templ += nums[m - 1 - i]
        mid_maxl = max(mid_maxl, templ)
        tempr += nums[m + i]
        mid_maxr = max(mid_maxr, tempr)
    # n 为奇数的时候，上面的循环会漏掉最后一个元素
    if n % 2 != 0:
        tempr += nums[n - 1]
        mid_maxr = max(mid_maxr, tempr)
    maxmid = mid_maxl + mid_maxr
    # 返回全局的最大子序和
    return max(maxleft, maxmid, maxright)


if __name__ == '__main__':
    ans = maxSubArray2([-2, -1, 2, 0, 1, 3, 1])
    print(ans)
