"""
剑指 Offer 07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

        3
       / \
      9  20
        /  \
       15   7


限制：
    0 <= 节点个数 <= 5000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    """
    :param preorder: List[int]
    :param inorder: List[int]
    :return: TreeNode
    """
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    r_idx = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:r_idx + 1], inorder[:r_idx])
    root.right = buildTree(preorder[r_idx + 1:], inorder[r_idx + 1:])
    return root
