#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void BFS(vector<vector<int>>& graph, int start) {
    int numVertices = graph.size();
    vector<bool> visited(numVertices, false); 
    queue<int> q;

    visited[start] = true; 
    q.push(start);

    while (!q.empty()) {
        int currentVertex = q.front();
        cout << currentVertex << " ";
        q.pop();


        for (int i = 0; i < graph[currentVertex].size(); ++i) {
            int adjacentVertex = graph[currentVertex][i];
            if (!visited[adjacentVertex]) {
                visited[adjacentVertex] = true;
                q.push(adjacentVertex);
            }
        }
    }
}

int main() {
    int numVertices, numEdges;
    cout << "Enter the number of vertices: ";
    cin >> numVertices;
    cout << "Enter the number of edges: ";
    cin >> numEdges;

    vector<vector<int>> graph(numVertices); 
    cout << "Enter the edges (format: u v) where u and v are vertices of the graph:\n";
    for (int i = 0; i < numEdges; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u); 
    }

    int startVertex;
    cout << "Enter the starting vertex for BFS: ";
    cin >> startVertex;

    cout << "BFS Traversal starting from vertex " << startVertex << ": ";
    BFS(graph, startVertex);

    return 0;
}
