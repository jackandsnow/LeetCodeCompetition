"""
剑指 Offer 12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，
每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：

    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true

示例 2：

    输入：board = [["a","b"],["c","d"]], word = "abcd"
    输出：false

提示：
    1 <= board.length <= 200
    1 <= board[i].length <= 200
"""


def has_path(board, word, row, col, flag):
    """
    :param board: List[List[str]]
    :param word: str
    :param row: int
    :param col: int
    :param flag: List[List[bool]]
    :return: bool
    """
    if not word:
        return True
    pos_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    m, n = len(board), len(board[0])
    for pos in pos_list:
        r, c = row + pos[0], col + pos[1]
        # 边界检查 + 是否访问过 + 首字母匹配
        if 0 <= r < m and 0 <= c < n and not flag[r][c] and board[r][c] == word[0]:
            flag[r][c] = True
            if has_path(board, word[1:], r, c, flag):
                return True
            else:   # 回溯
                flag[r][c] = False
    return False


def exist(board, word):
    """
    :param board: List[List[str]]
    :param word: str
    :return: bool
    """
    if word:
        # M * N 的矩阵
        m, n = len(board), len(board[0])
        flag = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag[i][j] = True
                    if has_path(board, word[1:], i, j, flag):
                        return True
                    else:   # 回溯
                        flag[i][j] = False
    return False
