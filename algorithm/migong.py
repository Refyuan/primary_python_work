class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.step=0
        self.current_step=""

graph=[]
while True:
    line = input()
    if line:
        graph.append(list(line))
    else:
        break

row = len(graph)
col = len(graph[0])
visit=[None]*row
for i in range(row):
    visit[i]=[False] * col

directions={"D":[1,0],'L':[0,-1],'R':[0,1],'U':[-1,0]}
queue=[]
start=Point(0,0)
visit[start.x][start.y]=True
queue.append(start)

while queue:
    cur=queue.pop(0)
    if cur.x == row - 1 and cur.y == col - 1:
        print(cur.current_step)
        break


    for direction in directions:
        next_x=cur.x+directions[direction][0]
        next_y = cur.y + directions[direction][1]

        if 0 <= next_x < row and 0 <= next_y < col and not visit[next_x][next_y] and graph[next_x][next_y]=='0':
            visit[next_x][next_y]=True
            next_point=Point(next_x,next_y)
            next_point.current_step=cur.current_step+direction
            print(direction)
            queue.append(next_point)