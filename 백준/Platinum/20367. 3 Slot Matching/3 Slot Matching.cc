#pragma GCC optimize("O3") 
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma") 
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native") 
#pragma GCC optimization ("unroll-loops")
#include <bits/stdc++.h>

using namespace std;

long long int A[3005];
long long int dp[3005][3005];

int main() 
{
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int n,t;

	cin >> n;
	
	for(int i=1;i<=n;i++)
	{
		cin >> A[i];
	}

	memset(dp,-1,sizeof(dp));
	
	dp[0][0] = 0;
	
	for(int i=1;i<=n;i++)
	{
		if(dp[i-1][0]!=-1)
		{
			dp[i][i] = max(dp[i][i],dp[i-1][0]);
		}
		for(int j=1;j<i;j++)
		{
			if(dp[i-1][j]==-1) continue;
			dp[i][0] = max(dp[i][0],dp[i-1][j] + A[i]*A[j]);
		}
		if(i-2>=0)
		{
			for(int j=1;j<i-1;j++)
			{
				if(dp[i-2][j]==-1) continue;
				dp[i][j] = max(dp[i][j],dp[i-2][j] + A[i-1]*A[i]);
				dp[i][i-1] = max(dp[i][i-1],dp[i-2][j] + A[i]*A[j]);
				dp[i][i] = max(dp[i][i],dp[i-2][j] + A[i-1]*A[j]);
			}
			if(dp[i-2][0]!=-1)
			{
				dp[i][0] = max(dp[i][0],dp[i-2][0] + A[i-1]*A[i]);
			}
		}
	}


	long long int res = 0;
	
	for(int i=0;i<=n;i++)
	{
		res = max(res,dp[n][i]);
	}
	
	cout << res << '\n';
	
	return 0;
}