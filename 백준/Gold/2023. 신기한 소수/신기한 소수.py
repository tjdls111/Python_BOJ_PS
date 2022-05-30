import sys

input = sys.stdin.readline

N = int(input())

sosus = [[0] for _ in range(9)]

sosus[1].extend([2, 3, 5, 7])


def check_sosu(num: int) -> bool:
    for k in range(2, int(num ** 0.5) + 1):
        if num % k == 0:
            return False
    return True


for i in range(2, N + 1):
    for j in sosus[i - 1]:
        if j == 0:
            continue
        for k in range(1, 10):
            if k == 0:
                continue
            tmp1 = int(str(j) + str(k))
            if check_sosu(tmp1):
                sosus[i].append(tmp1)
    
answer = sorted(list(set(sosus[N])))
for i in range(1, len(answer)):
    print(answer[i])
