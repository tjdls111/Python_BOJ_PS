import sys
input = sys.stdin.readline

first = input().rstrip()
second=input().rstrip()
dp=[[0]*(len(second)+1) for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1,len(second)+1):
        if first[i-1] == second[j-1]: # 같으면
            dp[i][j] = dp[i-1][j-1]+1 # 그전까지 LCS 길이+1
        else: # 다르면
            dp[i][j] = max(dp[i][j-1],dp[i-1][j]) # 그전까지 LCS 길이


print(dp[-1][-1])