#include <bits/stdc++.h>
using namespace std;

vector<int> aStarSearch(vector<vector<int>> edges,
        int src, int target, int n, vector<int> heuristic, int &finalCost) {

    vector<vector<pair<int,int>>> adj(n);
    for (int i = 0; i < (int)edges.size(); i++) {
        adj[edges[i][0]].push_back({edges[i][1], edges[i][2]});
        adj[edges[i][1]].push_back({edges[i][0], edges[i][2]});
    }

    vector<bool> visited(n, false);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({heuristic[src], src});

    vector<int> g(n, INT_MAX);
    g[src] = 0;

    vector<int> parent(n, -1);

    while (!pq.empty()) {
        int node = pq.top().[1];
        pq.pop();

        if (visited[node]) continue;
        visited[node] = true;

        if (node == target) break;

        for (auto edge : adj[node]) {
            int neigh = edge.first;
            int cost = edge.second;

            if (g[node] + cost < g[neigh]) {
                g[neigh] = g[node] + cost;
                parent[neigh] = node;
                int f = g[neigh] + heuristic[neigh];
                pq.push({f, neigh});
            }
        }
    }

    if (g[target] == INT_MAX) {
        finalCost = -1;
        return {};
    }

    finalCost = g[target];
    vector<int> path;
    int curr = target;
    while (curr != -1) {
        path.push_back(curr);
        curr = parent[curr];
    }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    int n = 14, source, target;
    vector<vector<int>> edgeList = {
        {0, 1, 3}, {0, 2, 6}, {0, 3, 5},
        {1, 4, 9}, {1, 5, 8}, {2, 6, 12},
        {2, 7, 14}, {3, 8, 7}, {8, 9, 5},
        {8, 10, 6}, {9, 11, 1}, {9, 12, 10},
        {9, 13, 2}
    };

    cout << "Enter the source node: ";
    cin >> source;
    cout << "Enter the destination node: ";
    cin >> target;


    vector<int> heuristic = {7, 6, 5, 6, 5, 4, 7, 8, 3, 0, 2, 1, 4, 3};


    if (source < 0 || source >= n || target < 0 || target >= n) {
        cout << "Invalid source or destination node!\n";
        return 0;
    }

    int finalCost;
    vector<int> path = aStarSearch(edgeList, source, target, n, heuristic, finalCost);

    cout << "The final Path is: ";
    for (int node : path) cout << node << " ";
    cout << "\nTotal cost = " << finalCost << "\n";

    return 0;
}

