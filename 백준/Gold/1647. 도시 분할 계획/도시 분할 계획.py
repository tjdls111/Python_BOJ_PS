import sys

input = sys.stdin.readline


def find_group(x):
    if parent[x] != x:  # 루트 노드면
        parent[x] = find_group(parent[x])
    return parent[x]


def union_group(a, b):
    a = find_group(a)
    b = find_group(b)
    # 작은 쪽 부모를 기준으로 같은 부모로(같은 그룹) 만들기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())  # 집(노드), 길(간선)
parent = [0] * (N + 1)  # 부모(그룹) 테이블

# 각자 자기를 부모로(그룹으로) 세팅
for i in range(N+1):
    parent[i] = i

my_roads = []  # 집집이 연결되게 하는, 유지비가 적게 드는 길들
all_roads = list(tuple(map(int, input().split())) for _ in range(M))
all_roads.sort(key=lambda x: x[2])  # 유지비 적게 드는 순으로 정렬

for road in all_roads:  # 길 정보 하나씩 보기
    a, b, cost = road  # a집, b집을 연결, 비용
    # a집과 b집이 연결되었으면(같은 그룹이면)
    if find_group(a) == find_group(b):
        continue  # 이 길은 필요 없다.
    else:  # 연결이 안되었으면
        my_roads.append(cost)  # 이 비용 쓰기
        union_group(a, b)  # 두 집 연결

my_roads.sort()  # 모든 집 연결할 때, 길 유지비 최소로 할 때 필요한 길들의 비용
# 젤 비싼 거 없애기 -> 그러면 마음이 두 쪽으로 분리됨.
ans = sum(my_roads[:-1])
print(ans)
