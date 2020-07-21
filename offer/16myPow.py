"""
剑指 Offer 16. 数值的整数次方
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:

    输入: 2.00000, 10
    输出: 1024.00000

示例 2:

    输入: 2.10000, 3
    输出: 9.26100

示例 3:

    输入: 2.00000, -2
    输出: 0.25000
    解释: 2-2 = 1/22 = 1/4 = 0.25
"""


def myPow(x, n):
    """
    :param x: float
    :param n: int
    :return: float
    """
    if n < 0:
        n = -n
        x = 1 / x
    ans = 1.0
    while n:
        # 奇数次方
        if n & 1:
            ans *= x
        x *= x
        # 乘的次数
        n //= 2
    return ans
