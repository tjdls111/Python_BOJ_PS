import sys

input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

R, C = map(int, input().split())
board = list(input().strip() for _ in range(R))

ans = 0

# visited = [[False] * C for _ in range(R)]

def dfs(i, j,cnt):
    global ans
    for k in range(4):
        ni, nj = i + directions[k][0], j + directions[k][1]
        if 0 <= ni < R and 0 <= nj < C and history[ord(board[ni][nj])-65] == False:  # 범위  체크, 알파벳 겹치나
            tmp = ord(board[ni][nj])-65
            history[tmp] = True
            # visited[ni][nj] = True
            dfs(ni, nj,cnt+1)
            history[tmp] = False
            # visited[ni][nj] = False
        else:
            ans = max(ans, cnt)
            

history = [False]*26
history[ord(board[0][0])-65] = True
# visited[0][0]=True
dfs(0, 0,1)

print(ans)
    