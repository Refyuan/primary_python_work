if __name__ == '__main__':

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            # 从起点到该点的步数
            self.step = 0
            # 到达该点位使用的方向
            self.current_step = ""

        def __repr__(self):
            return f"({self.x}, {self.y})"


    graph = []
    while True:
        line = input()
        if line:
            graph.append(list(line))
        else:
            break
    row = len(graph)
    col = len(graph[0])
    print(row, " ", col)
    # 定义一个地图大小的visited数组 记录是否走过
    visited = []
    for i in range(row):
        visited.append([False] * col)

    # 定义一个方向数组
    directions = {"D": [1, 0], "L": [0, -1], "R": [0, 1], "U": [-1, 0]}

    # 定义一个队列
    queue = []
    # 定义一个起点
    start = Point(0, 0)
    visited[start.x][start.y] = True
    queue.append(start)

    while queue:
        current = queue.pop(0)
        # 出口
        if current.x == row - 1 and current.y == col - 1:
            print("走的总步数", current.step)
            print("走的路径", current.current_step)
            break

        for direction in directions.keys():
            next_x = current.x + directions[direction][0]
            next_y = current.y + directions[direction][1]
            if 0 <= next_x < row and 0 <= next_y < col and not visited[next_x][next_y] and graph[next_x][next_y] == "0":
                visited[next_x][next_y] = True
                next_point = Point(next_x, next_y)
                next_point.step = current.step + 1
                next_point.current_step = current.current_step + direction
                queue.append(next_point)