"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    给定 word = "ABCCED", 返回 true.
    给定 word = "SEE", 返回 true.
    给定 word = "ABCB", 返回 false.

"""


def backtrack(board, index, word, flag):
    # word为空，则全部匹配完
    if not word:
        return True

    row, column = len(board), len(board[0])
    # 先匹配右边，再匹配下边，再匹配左边，最后匹配上边
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        i = index[0] + direction[0]
        j = index[1] + direction[1]
        # i, j 有效性检查 and 是否访问检查 and 是否匹配首字母
        if 0 <= i < row and 0 <= j < column and not flag[i][j] and board[i][j] == word[0]:
            flag[i][j] = True
            if backtrack(board, [i, j], word[1:], flag):
                return True
            else:
                # 回溯
                flag[i][j] = False
    return False


def exist(board, word):
    """
    回溯法
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    row, column = len(board), len(board[0])
    # 特殊情况
    if len(word) > row * column:
        return False

    # 用于标记每个元素是否被用过
    flag = [[False] * column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            if board[i][j] == word[0]:
                flag[i][j] = True
                if backtrack(board, [i, j], word[1:], flag):
                    return True
                else:
                    # 回溯
                    flag[i][j] = False
    return False


if __name__ == '__main__':
    ans = exist(
        board=[
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'E', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        word="ABCESEFSADE"
    )
    print(ans)
