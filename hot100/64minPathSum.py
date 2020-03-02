"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。

"""


def minPathSum(grid):
    """
    自顶向下的动态规划
    :type grid: List[List[int]]
    :rtype: int
    """
    m, n = len(grid), len(grid[0])
    # 边界条件，只有一行或一列
    if m == 1:
        return sum(grid[0])
    if n == 1:
        return sum(map(lambda x: x[0], grid))

    dp = [[-1] * n for _ in range(m)]
    dp[-1][-1] = grid[-1][-1]
    for i in range(m - 1, 0, -1):
        for j in range(n - 1, 0, -1):
            # 往上走
            if dp[i][j - 1] == -1:
                dp[i][j - 1] = grid[i][j - 1] + dp[i][j]
            # 往左走
            if dp[i - 1][j] == -1:
                dp[i - 1][j] = grid[i - 1][j] + dp[i][j]
            # 往左上角走
            dp[i - 1][j - 1] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[0][0]


if __name__ == '__main__':
    ans = minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ])
    print(ans)
