#include <bits/stdc++.h>

using namespace std;

vector <int> adj[60];
int n;
bool visited[60];
int res = 0;
bool flag = true;
bool flag2 = true;
void dfs(int now,int prev)
{
	if(adj[now].size() >= 3)
	{
		flag2 = false;
	}
	for(auto next : adj[now])
	{
		if(visited[next])
		{
			if(prev!=next)
			{
				flag = false;
			}
		}
		else
		{
			visited[next] = true;
			dfs(next,now);
		}
	}
}

int main() 
{
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int x1[60];
	int y1[60];
	int x2[60];
	int y2[60];	
	
	cin >> n;
	
	for(int i=0;i<n;i++)
	{
		cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];	
	}
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(i==j) continue;
			if((x1[i]==x1[j] && y1[i]==y1[j]) || (x1[i]==x2[j] && y1[i]==y2[j]) || (x2[i]==x1[j] && y2[i]==y1[j]) || (x2[i]==x2[j] && y2[i]==y2[j]))
			{
				//cout << i << ' ' << j << '\n';
				adj[i].push_back(j);
			}
		}
	}
	
	memset(visited,false,sizeof(visited));
	for(int i=0;i<n;i++)
	{
		if(!visited[i])
		{
			//cout << i << '\n';
			visited[i] = true;
			flag = true;
			flag2 = true;
			dfs(i,-1);
			if(!flag && flag2) res++;
		}
	}
	
	cout << res << '\n';
	
	return 0;
}