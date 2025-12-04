#include <iostream>
#include <vector>
#include <queue>
using namespace std;

bool vis[100];
vector<vector<int>> vec(100);

int main() {
    int v, e;
   cout << "Enter the number of vertices: ";
    cin >> v;
    cout << "Enter the number of edges: ";
    cin >> e;
 cout << "Enter the edges (format: v e):" << endl;

    for (int i = 0; i < e; i++) {
        int x, y;
        cin >> x >> y;
        vec[x].push_back(y);
    }

     cout << "BFS traversal starting from Vertice 0:" << endl;
    queue<int> q;
    q.push(0);
    vis[0] = true;

    while (!q.empty()) {
        int item = q.front();
        q.pop();
        cout << item << " ";

        for (auto u : vec[item]) {
            if (!vis[u]) {
                vis[u] = true;
                q.push(u);
            }
        }
    }

    return 0;
}