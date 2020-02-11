"""
22. 括号生成

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

"""


def help(st):
    if not st:
        return {'()'}

    result = set()
    for s in st:
        for i in range(len(s)):
            result.add(s[:i+1] + '()' + s[i+1:])
    return result


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = set()
    while n > 0:
        result = help(result)
        n -= 1
    return list(result)


if __name__ == '__main__':
    ans = generateParenthesis(3)
    print(ans)
    print(len(ans))
