"""
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

    输入：m = 2, n = 3, k = 1
    输出：3

示例 2：

    输入：m = 3, n = 1, k = 0
    输出：1

提示：
    1 <= n,m <= 100
    0 <= k <= 20
"""


def go(x, y, m, n, k, flag):
    if 0 <= x < m and 0 <= y < n and not flag[x][y]:
        a1, a2 = x // 10, x % 10
        b1, b2 = y // 10, y % 10
        if sum([a1, a2, b1, b2]) <= k:
            flag[x][y] = True
            return 1 + go(x + 1, y, m, n, k, flag) + go(x, y + 1, m, n, k, flag)
    return 0


def movingCount(m, n, k):
    """
    :param m: int
    :param n: int
    :param k: int
    :return: int
    """
    flag = [[False] * n for _ in range(m)]
    cnt = go(0, 0, m, n, k, flag)
    return cnt
