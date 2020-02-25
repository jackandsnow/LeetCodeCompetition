"""
面试题04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

给定 target = 5，返回 true。

给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000

"""


def findNumberIn2DArray1(matrix, target):
    """
    哈希
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    n = len(matrix)
    for i in range(n):
        dic = dict.fromkeys(matrix[i])
        if target in dic:
            return True
    return False


def findNumberIn2DArray2(matrix, target):
    """
    线性查找
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    n = len(matrix)
    # 判断数组是否为空
    if n > 0 and len(matrix[0]) > 0:
        m = len(matrix[0])
        # 首先判断右上角元素，然后向左下方查找
        i, j = 0, m - 1
        while i <= n - 1 and j >= 0:
            if target == matrix[i][j]:
                return True
            # 向左查找
            elif target < matrix[i][j]:
                j -= 1
            # 向下查找
            else:
                i += 1
    return False


if __name__ == '__main__':
    ans = findNumberIn2DArray2([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5)
    print(ans)
