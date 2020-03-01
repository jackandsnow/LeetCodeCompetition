"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:

    输入: [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

"""


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals:
        return []
    # 首先根据区间的下界进行排序
    intervals.sort()
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        temp = result[-1]
        # 区间有交集，则更新区间
        if temp[1] >= intervals[i][0]:
            result[-1] = [min(temp[0], intervals[i][0]), max(temp[1], intervals[i][1])]
        # 否则新增区间
        else:
            result.append(intervals[i])
    return result


if __name__ == '__main__':
    ans = merge([
        [1, 3], [2, 6], [8, 10], [15, 18]
    ])
    print(ans)
