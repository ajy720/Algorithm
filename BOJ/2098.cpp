#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_INT = INT32_MAX >> 1;

int dfs(int n, const vector<vector<int>> &graph, vector<vector<int>> &dp, int node, int visit)
{
    if (visit == (1 << n) - 1)
    {
        return graph[node][0] ? graph[node][0] : MAX_INT;
    }

    if (dp[node][visit] != -1)
    {
        return dp[node][visit];
    }

    dp[node][visit] = MAX_INT;
    for (int next_node = 0; next_node < n; next_node++)
    {
        // node에서 next_node로 가는 경로가 없거나 이미 방문한 노드인 경우 패스
        if (graph[node][next_node] == 0 || (visit & (1 << next_node)))
            continue;

        // 아닌 경우, 그 경로로 갔을 때를 가정하고 최적값 구하기
        int next_visit = visit | (1 << next_node);

        int cost = dfs(n, graph, dp, next_node, next_visit) + graph[node][next_node];
        dp[node][visit] = min(dp[node][visit], cost);
    }

    return dp[node][visit];
}

int travelling(int n, const vector<vector<int>> &graph)
{
    vector<vector<int>> dp(n, vector<int>((1 << n) - 1, -1));

    return dfs(n, graph, dp, 0, 1);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> cost_graph(N, vector<int>(N));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> cost_graph[i][j];
        }
    }

    int ans = travelling(N, cost_graph);
    cout << ans << '\n';

    return 0;
}