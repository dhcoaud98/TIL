min_v = 999999999
input_list = [1, 2, 3]
visited = [] * len(input_list)

def BFS(i, g, c):  # i: 방문하는 노드, g: 도착지, c: 지나온 정점 갯수)
    global min_v
    if i == g: # 목적지에 도착한 경우
        if min_v > c:
            min_v = c
            return min_v
    else:
        visited[i] = 1  # 방문 체크
        for j in input_list[:]:
            BFS(j, g, c+1)
        visited[i] = 0


print(BFS(0, 1, 0))