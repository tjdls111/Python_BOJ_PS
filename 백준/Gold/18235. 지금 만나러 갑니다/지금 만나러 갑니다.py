'''
18235: 지금 만나러 갑니다
https://www.acmicpc.net/problem/18235
'''

import sys, collections

input = sys.stdin.readline().rstrip

N, A, B = map(int, input().split())

q = collections.deque()
now_5_ri = set()

q.append((0, A, '5'))  # 몇번 점프, 오리 위치, 이름
q.append((0, B, '6'))  # 몇번 점프, 육리 위치, 이름

now_cnt = 0
flag = False
ans = 0
while q:
    jump_cnt, idx, name = q.popleft()


    if name == '6':  # 육리는 오리를 찾기
        # 점프 횟수가 바뀌면
        if now_cnt != jump_cnt:
            tmp1 = idx + 2 ** jump_cnt
            tmp2 = idx - 2 ** jump_cnt
            if 0 < tmp1 <= N:
                q.append((jump_cnt + 1, tmp1, '6'))
            if 0 < tmp2 <= N:
                q.append((jump_cnt + 1, tmp2, '6'))

        else: # 점프 횟수 같을 때

            tmp1 = idx + 2 ** jump_cnt
            tmp2 = idx - 2 ** jump_cnt

            if tmp1 in now_5_ri or tmp2 in now_5_ri:  # 만났으면
                flag = True
                ans = jump_cnt
                break
            else:  # 못 만났으면
                if 0 < tmp1 <= N:
                    q.append((jump_cnt + 1, tmp1, '6'))
                if 0 < tmp2 <= N:
                    q.append((jump_cnt + 1, tmp2, '6'))

    else:  # 오리면 자기 자리 표시하도록
        # 점프 횟수가 바뀌면
        if now_cnt != jump_cnt:
            now_5_ri = set()  # 오리 위치 초기화
            now_cnt = jump_cnt

        tmp1 = idx + 2 ** jump_cnt
        tmp2 = idx - 2 ** jump_cnt

        if 0 < tmp1 <= N:
            now_5_ri.add(tmp1)
            q.append((jump_cnt + 1, tmp1, '5'))

        if 0 < tmp2 <= N:
            now_5_ri.add(tmp2)
            q.append((jump_cnt + 1, tmp2, '5'))

if flag:
    print(ans+1)
else:
    print(-1)
