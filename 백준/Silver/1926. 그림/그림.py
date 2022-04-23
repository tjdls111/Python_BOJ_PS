import sys, collections

input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

picture_max_width = 0
picture_cnt = 0

n, m = map(int, input().split())
arr = list(input().split() for _ in range(n))

def bfs(i, j):
    global now_picture_width
    q = collections.deque()
    q.append((i,j))

    while q :
        i, j =q.popleft()

        for k in range(4):
            ni, nj = i + directions[k][0], j + directions[k][1]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '1':  # 이어진 그림이라면
                now_picture_width += 1
                arr[ni][nj] = '0' # 다시 방문하지 않도록
                q.append((ni,nj))

for i in range(n):
    for j in range(m):
        if arr[i][j]=='1':  # 새로운 그림이라면
            picture_cnt += 1
            now_picture_width =1
            arr[i][j] = '0'# 다시 방문하지 않도록
            bfs(i, j)
            picture_max_width = max(picture_max_width,now_picture_width)

print(picture_cnt)
print(picture_max_width)
