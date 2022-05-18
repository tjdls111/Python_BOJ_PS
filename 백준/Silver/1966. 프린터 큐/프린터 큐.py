import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    origin_papers = list(map(int, input().split()))

    priority = deque(sorted(origin_papers, reverse=True))

    papers = deque()
    for i in range(N):
        papers.append((origin_papers[i], i))

    print_cnt = 0
    while papers:
        tmp_paper_priority, tmp_paper_idx = papers.popleft()
        now_paper_priority = priority[0]

        if tmp_paper_priority == now_paper_priority:  # 이 문서가 제일 우선순위 높은 문서이면
            print_cnt += 1  # 프린트
            priority.popleft()  # 그 우선순위 제거
            if tmp_paper_idx == M:  # 몇번째로 인쇄되었는지 궁금한 문서이면
                print(print_cnt)  # 출력
                break
        else:  # 이것보다 더 우선순위 높은 문서가 있으면
            papers.append((tmp_paper_priority, tmp_paper_idx))  # 그 문서 마지막으로 보내기
