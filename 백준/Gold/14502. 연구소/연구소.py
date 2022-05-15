import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())

arr_origin = list(list(map(int, input().split())) for _ in range(N))

candidates = list(combinations(range(N * M), 3))

ans = 0

for candidate in candidates:
    arr = deepcopy(arr_origin)
    # 새로 세울 3개의 벽
    new_wall_1, new_wall_2, new_wall_3 = candidate
    new_wall_1_i, new_wall_1_j = new_wall_1 // M, new_wall_1 % M
    new_wall_2_i, new_wall_2_j = new_wall_2 // M, new_wall_2 % M
    new_wall_3_i, new_wall_3_j = new_wall_3 // M, new_wall_3 % M

    # 빈 칸에만 벽을 세울 수 있음
    if arr[new_wall_1_i][new_wall_1_j]==0 and arr[new_wall_2_i][new_wall_2_j]==0 and arr[new_wall_3_i][new_wall_3_j]==0:

        # 그 부분 벽으로 만들기
        arr[new_wall_1_i][new_wall_1_j] = 1
        arr[new_wall_2_i][new_wall_2_j] = 1
        arr[new_wall_3_i][new_wall_3_j] = 1

        # 이 상태에서 바이러스가 퍼진다
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                # 방문 안했고 바이러스가 있으면
                if visited[i][j] == False and arr[i][j] == 2:
                    # 감염시킬 수 있는 건 다 감염 시키기!
                    q = deque()
                    q.append((i, j))
                    while q:
                        ii, jj = q.popleft()
                        for k in range(4):
                            ni, nj = directions[k][0] + ii, directions[k][1] + jj
                            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]==False:
                                # 범위, 방문 체크
                                if arr[ni][nj] == 0: # 빈칸이면 바이러스 퍼짐
                                    arr[ni][nj] = 2
                                    q.append((ni, nj))
                                    visited[ni][nj] = True
                                # elif arr[ni][nj] == 1: # 벽이면 넘어감
                                #     continue
                                # elif arr[ni][nj] == 2:
                                #     q.append((ni, nj))
                                #     visited[ni][nj] = True
        # 안전 구역 수 세고, 정답 업데이트하기
        safe_zone_cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    safe_zone_cnt += 1

        ans = max(ans, safe_zone_cnt)
print(ans)
