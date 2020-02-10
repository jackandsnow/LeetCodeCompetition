"""
11. 盛最多水的容器
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

    输入: [1,8,6,2,5,4,8,3,7]
    输出: 49

"""


def violent_method(height):
    """
    暴力法，计算出任何两线段围成的矩形面积
    然后再取出最大的面积
    """
    n = len(height)
    maxa = 0
    for i in range(n):
        for j in range(i + 1, n):
            temp = abs(i - j) * min(height[i], height[j])
            if maxa < temp:
                maxa = temp
    return maxa


def maxArea(height):
    """
    双指针法
    :type height: List[int]
    :rtype: int
    """
    l = 0
    r = len(height) - 1
    result = 0
    while l < r:
        result = max(result, (r - l) * min(height[l], height[r]))
        # 较短线段向中间移动，能够获得更大的面积
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return result


if __name__ == '__main__':
    ans = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(ans)
