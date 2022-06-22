import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

N=int(input())

rice_cakes_per_day = [] * N
for k in range(N):
    rice_cake = input().split()[1:]
    rice_cakes_per_day.append(rice_cake)

def dfs(day, history):
    global flag
    if flag:
        return

    if day == N:
        print('\n'.join(history.split()))
        flag = True
        return

    for cake in rice_cakes_per_day[day]: # 그 날의 떡 보면서
        # 첫날이라면
        if day == 0:
            visited[day+1][int(cake)] = True
            dfs(day+1, history+cake+' ') # 무조건 그 떡을 주고, 다음날로 넘어가기
            # visited[day+1][int(cake)] = False

        # 첫날 아닌데 전날과 안 겹치고 방문 안 했으면
        elif cake != history[-2] and not visited[day+1][int(cake)]:
            visited[day+1][int(cake)] = True
            dfs(day+1, history+cake+' ') # 그 떡을 주고, 다음날로 넘어가기
            # visited[day+1][int(cake)] = False


visited = [[False]*10 for _ in range(N+1)] # 날짜, 전날 준 떡
flag = False
dfs(0,'')

if flag == False: # 떡 줄 방법이 없으면 -1 출력
    print(-1)