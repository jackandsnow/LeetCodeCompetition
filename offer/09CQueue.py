"""
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

    输入：
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出：[null,null,3,-1]

示例 2：

    输入：
    ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
    [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]

提示：
    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用
"""


class CQueue:

    def __init__(self):
        self.data_stack = []
        self.delete_stack = []

    def appendTail(self, value):
        """
        :param value: int
        :return: None
        """
        self.data_stack.append(value)

    def deleteHead(self):
        """
        :return: int
        """
        ans = -1
        if self.data_stack:
            while self.data_stack:
                last = self.data_stack.pop()
                self.delete_stack.append(last)

            ans = self.delete_stack.pop()
            while self.delete_stack:
                last = self.delete_stack.pop()
                self.data_stack.append(last)
        return ans

    def deleteHead2(self):
        """
        :return: int
        """
        if not self.data_stack and not self.delete_stack:
            return -1

        if not self.delete_stack:
            while self.data_stack:
                last = self.data_stack.pop()
                self.delete_stack.append(last)

        ans = self.delete_stack.pop()
        return ans

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
