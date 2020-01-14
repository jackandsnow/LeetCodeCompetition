"""
1318. 或运算的最小翻转次数

给你三个正整数 a、b 和 c。

你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。

示例 1：

0010->a         0001->a
0110->b         0100->b
----     ——>    ----
0101->c         0101->c

    输入：a = 2, b = 6, c = 5
    输出：3
    解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c

示例 2：

    输入：a = 4, b = 2, c = 7
    输出：1

示例 3：

    输入：a = 1, b = 2, c = 3
    输出：0
 

提示：

    1 <= a <= 10^9
    1 <= b <= 10^9
    1 <= c <= 10^9

"""


def add_zero(s, n):
    # 前面补 0 使位数对齐
    for i in range(n - len(s)):
        s = '0' + s
    return s


def minFlips(a, b, c):
    # 特殊情况
    if a == b == c:
        return 0

    # 首先转换为二进制，并补0对齐
    x = bin(a).replace('0b', '')
    y = bin(b).replace('0b', '')
    z = bin(c).replace('0b', '')
    maxlen = max([len(x), len(y), len(z)])
    x, y, z = map(lambda s: add_zero(s, maxlen), [x, y, z])
    # 保证按位【或运算相等】
    count = 0
    for i in range(maxlen):
        x1, y1, z1 = int(x[i]), int(y[i]), int(z[i])
        x2, y2 = abs(x1 - 1), abs(y1 - 1)
        # 需要进行位翻转
        if not (x1 or y1) == z1:
            # x 翻转
            if (x2 or y1) == z1:
                count += 1
            # y 翻转
            elif (x1 or y2) == z1:
                count += 1
            # x, y 都翻转
            else:
                count += 2
    return count


if __name__ == '__main__':
    ans = minFlips(1, 1, 2)
    print(ans)  # 3
