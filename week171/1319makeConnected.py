"""
1319. 连通网络的操作次数
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

示例 1：

    输入：n = 4, connections = [[0,1],[0,2],[1,2]]
    输出：1
    解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。

示例 2：

    输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    输出：2

示例 3：

    输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
    输出：-1
    解释：线缆数量不足。

示例 4：

    输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
    输出：0
 
提示：

    1 <= n <= 10^5
    1 <= connections.length <= min(n*(n-1)/2, 10^5)
    connections[i].length == 2
    0 <= connections[i][0], connections[i][1] < n
    connections[i][0] != connections[i][1]
    没有重复的连接。
    两台计算机不会通过多条线缆连接。

"""


def DFS(edge_list, start, curr, depth, visited):
    # 进入则标记该节点被访问
    visited[curr] = True
    # 求以 start 为起点的有几个环
    depth += 1
    count = 0
    for edge in edge_list[curr]:
        near_node = edge[1]
        # 找到环
        if near_node == start and depth > 2:
            # 返回时取消该节点的标记
            visited[curr] = False
            return 1
        elif not visited[near_node]:
            count += DFS(edge_list, start, near_node, depth, visited)
    # 返回时取消该节点的标记
    visited[curr] = False
    return count


def makeConnected(n, connections):
    """
    暴力法，性能太差
    :param n:
    :param connections:
    :return:
    """
    # 题目明确说了至少有一条线缆
    if n <= 2:
        return 0

    # 线缆不足
    if len(connections) < n - 1:
        return -1

    all_nodes = set(range(n))
    connected_nodes = set()
    edge_list = [[] * n for _ in range(n)]

    for _, con in enumerate(connections):
        [i, j] = con
        edge_list[i].append([i, j])
        edge_list[j].append([j, i])
        # 添加到已连通的节点
        connected_nodes.add(i)
        connected_nodes.add(j)

    # 全连通的
    if len(connected_nodes) == n:
        return 0

    # 孤立的节点
    alone_nodes = all_nodes.difference(connected_nodes)
    # print(alone_nodes)

    # 计算冗余的边数，比较其与孤立节点数的大小
    # 有几个封闭环就多几条边
    visited = [False] * n
    result = 0
    for node in connected_nodes:
        cnt = DFS(edge_list, start=node, curr=node, depth=0, visited=visited)
        result = max(result, cnt // 2)

    if len(alone_nodes) <= result:
        return len(alone_nodes)
    return -1


if __name__ == '__main__':
    ans = makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]])
    # ans = makeConnected(n=8, connections=[
    #     [0, 1], [0, 7], [0, 5], [1, 6], [1, 4], [1, 3], [2, 4], [4, 5], [5, 6]
    # ])
    print(ans)
