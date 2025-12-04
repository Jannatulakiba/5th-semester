 #include <bits/stdc++.h>
using namespace std;
vector<int> BestFirstSearch(vector<vector<int>> edges,
int src, int target, int n) {
    vector<vector<vector<int>>> adj(n);

    for (int i=0;i<edges.size();i++){
        adj[edges[i][0]].push_back({edges[i][1], edges[i][2]});
                adj[edges[i][1]].push_back({edges[i][0], edges[i][2]});
    }
    vector<bool>visited(n,false);
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    pq.push({0, src});
    visited[src]= true;
    vector<int> path;

    while(!pq.empty()){
        int x=pq.top()[1];
        path.push_back(x);
        pq.pop();
        if (x == target)
        break;

        for (int i=0; i<adj[x].size();i++){
            if(!visited [adj[x][i][0]]){
            visited [adj[x][i][0]]=true;
            pq.push({adj[x][i][1], adj[x][i][0]});

        }
        }
    }
    return path;
}
int main(){
    int n=14, target,source;
    vector<vector<int>>edgelist={
        {0,1,3},{0,2,6},{0,3,5},{1,4,9},
        {1,5,8},{2,6,12},{2,7,14},{3,8,7},
        {8,9,5},{8,10,6},{9,11,1},{9,12,10},{9,13,2}
    };
    cout << ("Enter the source code: ");
    cin >> source;
     cout << ("Enter the Destination code: ");
    cin >> target;

    if (source < 0 || source >= n || target < 0 || target >= n) {
    cout << "Invalid source or destination node!\n";
    return 0;
}

    vector<int>path=BestFirstSearch(edgelist, source,target,n);
     cout << "The final path is: ";
     for(int i=0;i<path.size();i++){
        cout<< path[i]<<" ";
    }
    return 0;

}
