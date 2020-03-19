"""
85. 最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

    输入:
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    输出: 6

"""


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


def maximalRectangle1(matrix):
    """
    将每一行看成84题的输入高度求解
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0

    result = 0
    n, m = len(matrix), len(matrix[0])
    dp = [0] * m
    for i in range(n):
        for j in range(m):
            dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
        result = max(result, largestRectangleArea(dp))
    return result


def maximalRectangle(matrix):
    """
    动态规划
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0

    result = 0
    n, m = len(matrix), len(matrix[0])
    left = [0] * m
    right = [m] * m
    height = [0] * m
    for i in range(n):
        curr_left, curr_right = 0, m
        # 计算每一列的最大高度和左边界
        for j in range(m):
            if matrix[i][j] == '1':
                left[j] = max(left[j], curr_left)
                height[j] = height[j] + 1
            else:
                left[j] = 0
                curr_left = j + 1
                height[j] = 0
        # 计算右边界
        for j in range(m - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], curr_right)
            else:
                right[j] = m
                curr_right = j
        # 计算面积
        for j in range(m):
            result = max(result, height[j] * (right[j] - left[j]))
    return result


if __name__ == '__main__':
    ans = maximalRectangle([["0", "1"], ["1", "0"]])
    # [
    #    ["1", "0", "1", "0", "0"],
    #     ["1", "0", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "0", "0", "1", "0"]
    # ])
    print(ans)
