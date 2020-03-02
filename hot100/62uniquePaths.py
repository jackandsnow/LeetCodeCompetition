"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

    输入: m = 3, n = 2
    输出: 3
    解释:
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向右 -> 向下
    2. 向右 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向右

示例 2:

    输入: m = 7, n = 3
    输出: 28
"""


def uniquePaths(m, n):
    """
    自顶向下的动态规划
    :type m: int
    :type n: int
    :rtype: int
    """
    # 边界条件，一行或一列
    if n == 1 or m == 1:
        return 1
    dp = [[0] * m for _ in range(n)]
    # 终点位置出发
    dp[n - 1][m - 1] = 1
    for i in range(n - 1, 0, -1):
        for j in range(m - 1, 0, -1):
            # 向上走
            dp[i-1][j] = max(dp[i-1][j], dp[i][j])
            # 向左走
            dp[i][j-1] = max(dp[i][j-1], dp[i][j])
            # 向左上角走
            dp[i-1][j-1] = dp[i-1][j] + dp[i][j-1]
    # 返回到达起点的总路径条数
    return dp[0][0]


if __name__ == '__main__':
    ans = uniquePaths(1, 2)
    print(ans)
