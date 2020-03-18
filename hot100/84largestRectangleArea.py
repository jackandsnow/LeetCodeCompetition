"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

    输入: [2,1,5,6,2,3]
    输出: 10

"""


def largestRectangleArea1(heights):
    """
    暴力法，超时，剩余3个样例未通过
    :type heights: List[int]
    :rtype: int
    """
    if not heights:
        return 0

    n = len(heights)
    result = 0
    for i in range(n):
        # 记录 i 到 j 之间的最低高度
        min_height = -1
        for j in range(i, n):
            if min_height == -1:
                min_height = heights[j]
            else:
                min_height = min(min_height, heights[j])
            result = max(result, min_height * (j - i + 1))
    return result


def largestRectangleArea(heights):
    """
    栈方法
    :type heights: List[int]
    :rtype: int
    """
    stack = [-1]
    result = 0
    for i, h in enumerate(heights):
        while stack[-1] != -1 and h <= heights[stack[-1]]:
            top = stack.pop()
            result = max(result, heights[top] * (i - stack[-1] - 1))
        # 当前高度更高，继续压栈
        stack.append(i)
    while stack[-1] != -1:
        top = stack.pop()
        result = max(result, heights[top] * (len(heights) - stack[-1] - 1))
    return result


if __name__ == '__main__':
    ans = largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(ans)
