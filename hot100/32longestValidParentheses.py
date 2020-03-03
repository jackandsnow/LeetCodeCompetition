"""
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"

示例 2:

    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"

"""


def longestValidParentheses(s):
    """
    动态规划方法
    :type s: str
    :rtype: int
    """
    maxlen = 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        # 处理右括号
        if s[i] == ')':
            # 匹配上左括号
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2 if i > 2 else 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 if i - dp[i - 1] >= 2 else dp[i - 1] + 2
            maxlen = max(maxlen, dp[i])
    return maxlen


if __name__ == '__main__':
    ans = longestValidParentheses(')(')
    print(ans)
