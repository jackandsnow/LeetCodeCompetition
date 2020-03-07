"""
72. 编辑距离
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

（1）插入一个字符
（2）删除一个字符
（3）替换一个字符

示例 1:

    输入: word1 = "horse", word2 = "ros"
    输出: 3
    解释:
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')

示例 2:

    输入: word1 = "intention", word2 = "execution"
    输出: 5
    解释:
    intention -> inention (删除 't')
    inention -> enention (将 'i' 替换为 'e')
    enention -> exention (将 'n' 替换为 'x')
    exention -> exection (将 'n' 替换为 'c')
    exection -> execution (插入 'u')

"""


def minDistance(word1, word2):
    """
    动态规划方法
    :type word1: str
    :type word2: str
    :rtype: int
    """
    n, m = len(word1), len(word2)
    # 任一个输入为空串
    if n * m == 0:
        return n + m

    # dp[i][j] 表示 word1 的前 i 个字母和 word2 的前 j 个字母之间的编辑距离
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 边界情况，一个空串与一个非空串
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 删除操作
            left = dp[i - 1][j] + 1
            # 插入操作
            down = dp[i][j - 1] + 1
            # 替换操作
            left_down = dp[i - 1][j - 1]
            # 两子串的最后一个字母若不相同，则需替换
            if word1[i - 1] != word2[j - 1]:
                left_down += 1
            dp[i][j] = min(left, down, left_down)
    return dp[n][m]


if __name__ == '__main__':
    ans = minDistance(word1="intention", word2="execution")
    print(ans)
