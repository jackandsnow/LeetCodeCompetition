"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

示例 1:

    输入: "()"
    输出: true

示例 2:

    输入: "()[]{}"
    输出: true

示例 3:

    输入: "(]"
    输出: false

示例 4:

    输入: "([)]"
    输出: false

示例 5:

    输入: "{[]}"
    输出: true

"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # 空字符串
    if not s:
        return True
    dic = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []
    for c in s:
        # 栈不为空
        if stack:
            top = dic.get(stack[-1])
            # 如果是右括号
            if not top:
                return False
            # 匹配栈顶左括号
            if c.__eq__(top):
                stack.pop()
            # 不匹配就压栈
            else:
                stack.append(c)
        else:
            stack.append(c)
    # 栈为空表示所有括号匹配
    return not stack


if __name__ == '__main__':
    ans = isValid('[()][]')
    print(ans)
