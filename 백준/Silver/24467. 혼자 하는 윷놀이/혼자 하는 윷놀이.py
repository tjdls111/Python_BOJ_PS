'''
24467: 혼자 하는 윳놀이
https://www.acmicpc.net/problem/24467
'''

import sys

input = sys.stdin.readline

course = 0
idx = 0

isWin = False
for i in range(10):
    yuk = sum(list(map(int, input().rstrip())))
    while yuk == 0 or yuk == 4:
        # 모두 뒷면: 4칸 -> 윷 다시
        if yuk == 0:
            idx += 4
        # 모두 앞면: 5칸 ->  윷 다시
        elif yuk == 4:
            idx += 5
        yuk = sum(list(map(int, input().rstrip())))

    if yuk == 3:  # 뒷면 하나: 1칸
        idx += 1
    elif yuk == 2:  # 뒷면 2: 2칸
        idx += 2
    elif yuk == 1:  # 뒷면 3: 3칸
        idx += 3

    # 0번으로 가다가
    if course == 0:
        # 1번 갈림길 만나면
        if idx == 5:
            course = 1
            idx = 0
        # 3번 갈림길 만나면
        elif idx == 10:
            course = 3
            idx = 0
        # 도착
        elif idx >= 21:
            isWin = True
    # 1번으로 가다가
    elif course == 1:
        # 2번 갈림길 만나면
        if idx == 3:
            course = 2
            idx = 0
        # 도착
        elif idx >= 12:
            isWin = True

    # 2번으로 가다가
    elif course == 2:

        # 도착
        if idx >= 4:
            isWin = True

    # 3번으로 가다가
    elif course == 3:
        # 도착
        if idx >= 7:
            isWin = True

# 승리 여부
if isWin:
    print('WIN')

else:
    print('LOSE')
