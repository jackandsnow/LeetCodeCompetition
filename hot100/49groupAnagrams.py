"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

    输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
    输出:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

"""


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = {}
    for i, s in enumerate(strs):
        # 每个字符串按照字母序排序
        ordered = ''.join((lambda x: (x.sort(), x))(list(s))[1])
        # 将字母序作为 key，实际值作为 value 存到字典
        if ordered not in dic:
            dic[ordered] = [strs[i]]
        else:
            dic[ordered].append(strs[i])
    # 将每个字母序的实际值取出返回
    return list(dic.values())


if __name__ == '__main__':
    ans = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)
