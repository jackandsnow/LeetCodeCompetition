"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶

示例 2：

    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶

"""


def climbStairs(n):
    """
    自顶向下的动态规划
    :type n: int
    :rtype: int
    """
    # 边界情况
    if n < 4:
        return n
    dp = [0] * n
    dp[-1] = 1
    dp[-2] = 2
    # 每次爬一阶或两阶
    for i in range(n - 3, -1, -1):
        dp[i] = dp[i + 1] + dp[i + 2]
    return dp[0]


if __name__ == '__main__':
    ans = climbStairs(8)
    print(ans)