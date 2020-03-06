"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6

"""


def trap(height):
    """
    双指针法
    :type height: List[int]
    :rtype: int
    """
    result = 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    while left < right:
        # 右端水柱更高，则从左往右计算积水高度
        if height[left] < height[right]:
            # 找到左端最高的水柱
            if height[left] >= left_max:
                left_max = height[left]
            # 当前水柱比左端最高水柱低，说明有积水
            else:
                result += left_max - height[left]
            left += 1
        # 反之，从右往左计算积水高度
        else:
            # 找到右端最高的水柱
            if height[right] >= right_max:
                right_max = height[right]
            # 当前水柱比右端最高水柱低，说明有积水
            else:
                result += right_max - height[right]
            right -= 1
    return result


if __name__ == '__main__':
    ans = trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(ans)
