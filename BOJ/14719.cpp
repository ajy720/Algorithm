#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int maxWater(vector<int> &arr)
{
    int n = arr.size();
    vector<int> leftMax(n), rightMax(n);

    int ans = 0;

    leftMax[0] = arr[0];
    for (int i = 1; i < n; i++)
    {
        leftMax[i] = max(leftMax[i - 1], arr[i]);
    }

    rightMax[n - 1] = arr[n - 1];
    for (int i = n - 2; i >= 0; i--)
    {
        rightMax[i] = max(rightMax[i + 1], arr[i]);
    }

    for (int i = 0; i < n; i++)
    {
        ans += min(rightMax[i], leftMax[i]) - arr[i];
    }

    return ans;
}

int main(int argc, char const *argv[])
{
    int test_num = 1;

    for (int t = 0; t < test_num; ++t)
    {
        int H, W;
        cin >> H >> W;

        vector<int> arr(W);
        for (int i = 0; i < W; ++i)
        {
            cin >> arr[i];
        }

        cout << maxWater(arr) << endl;
    }

    return 0;
}
