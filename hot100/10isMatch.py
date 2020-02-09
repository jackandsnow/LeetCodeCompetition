"""
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
· s 可能为空，且只包含从 a-z 的小写字母。
· p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:

    输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:

    输入:
    s = "aa"
    p = "a*"
    输出: true
    解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:

    输入:
    s = "ab"
    p = ".*"
    输出: true
    解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:

    输入:
    s = "aab"
    p = "c*a*b"
    输出: true
    解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:

    输入:
    s = "mississippi"
    p = "mis*is*p*."
    输出: false

"""


def backtrack_match(text, pattern):
    # 使用回溯法求解
    if not pattern:
        return not text
    # bool(text) 判断text是否为空
    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (backtrack_match(text, pattern[2:]) or
                first_match and backtrack_match(text[1:], pattern))
    else:  # 如果没有 '*'，则按位匹配即可
        return first_match and backtrack_match(text[1:], pattern[1:])


def dp_down_match(text, pattern):
    # 使用自底向上动态规划求解
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]

    return dp[0][0]


def dp_top_match(text, pattern):
    # 使用自顶向下动态规划求解
    result = {}

    def dp(i, j):
        if (i, j) not in result:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)
            result[i, j] = ans
        return result[i, j]

    return dp(0, 0)


def isMatch(s, p):
    return dp_down_match(s, p)
    # return backtrack_match(s, p)


if __name__ == '__main__':
    ans = isMatch('asa', '.*')
    print(ans)
