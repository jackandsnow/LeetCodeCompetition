"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明: 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

"""


def help(list1, list2):
    """
    实现两个字符数组的所有排列组合
    """
    result = []
    for s1 in list1:
        for s2 in list2:
            result.append(s1 + s2)
    return result


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # 空串判断
    if not digits:
        return []

    dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    result = dic.get(digits[0])
    i = 1
    while i < len(digits):
        result = help(result, dic.get(digits[i]))
        i += 1
    return result


if __name__ == '__main__':
    ans = letterCombinations('235')
    print(ans)
