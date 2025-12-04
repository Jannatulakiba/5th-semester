#include <bits/stdc++.h>
using namespace std;

int main() {
    int e;//edge
    cout<<"Enter the number of edge e: ";
    cin >> e;

    map<char, vector<pair<char,int>>> adj;
    set<char> nodes;

    for (int i = 0; i < e; i++) {
        char u, v; int w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        nodes.insert(u);
        nodes.insert(v);
    }

    char src, dest;
    cin >> src >> dest;



    const int INF = 1e9;
    map<char,int>  dist;
    map<char,char> parent;
    map<char,bool> vis;

    for (char x : nodes) {
        dist[x] = INF;
        parent[x] = '\0';
        vis[x] = false;
    }


    priority_queue<pair<int,char>, vector<pair<int,char>>, greater<pair<int,char>>> pq;
    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (vis[u]) continue;
        vis[u] = true;
        if (u == dest) break;

        for (auto [v, w] : adj[u]) {
            if (d + w < dist[v]) {
                dist[v] = d + w;
                parent[v] = u;
                pq.push({dist[v], v});
            }
        }
    }



    cout << "Cost from " << src << " to " << dest << " = " << dist[dest] << "\n";

    vector<char> path;
    for (char cur = dest; cur != '\0'; cur = parent[cur]) {
        path.push_back(cur);
        if (cur == src) break;
    }
    reverse(path.begin(), path.end());

    cout << "Path: ";
    for (char c : path) cout << c << ' ';
    cout << '\n';
    return 0;
}
