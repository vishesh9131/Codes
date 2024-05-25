#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void bfs(vector<vector<int>>& matrix){
    int rows = matrix.size();
    int col  = matrix[0].size();
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    while(!q.empty()){
        auto curr = q.front();
        q.pop();
        int x = curr.first;
        int y = curr.second;
        if(x<0 || x>=rows || y<0 || y>=col || matrix[x][y]==1) continue;
        matrix[x][y] = 1;
        q.push(make_pair(x+1, y));
        q.push(make_pair(x-1, y));
        q.push(make_pair(x, y+1));
        q.push(make_pair(x, y-1));
    }
}

int main(){
    vector<vector<int>> adj1(4, vector<int>(5, 0));
    adj1[0][1] = 0;
    adj1[0][2] = 1;
    adj1[0][3] = 1;
    adj1[0][4] = 1;


    adj1[1][1] = 1;
    adj1[1][2] = 0;
    adj1[1][3] = 1;
    adj1[1][4] = 0;


    adj1[2][1] = 0;
    adj1[2][2] = 1;
    adj1[2][3] = 0;
    adj1[2][4] = 1;


    adj1[3][1] = 1;
    adj1[3][2] = 0;
    adj1[3][3] = 1;
    adj1[3][4] = 0;



    bfs(adj1);
    for (int i = 0; i<2 ; i++){
        for (int j = 0; j<3 ; j++){
            cout<<adj1[i][j]<<" ";
        }
        cout<<endl;
    }
 }