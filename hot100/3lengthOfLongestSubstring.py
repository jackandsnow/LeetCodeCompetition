"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxn = 0
    # 保存当前最长的子串
    temp = ''
    for c in s:
        if c not in temp:
            temp += c
        else:
            maxn = max(maxn, len(temp))
            # 找到重复的字符，截断前面部分，末尾继续加
            temp = temp[temp.index(c) + 1:] + c
    # 若 s 只包含一个字符，则 maxn 无法更新
    return max(maxn, len(temp))


if __name__ == '__main__':
    ans = lengthOfLongestSubstring('pwwkew')
    print(ans)
