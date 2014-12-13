// Including standard libraries
#include <vector>
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int dfs(int root,
        vector<vector<int> >& edges,
        vector<int>& totSums,
        vector<int>& vals,
        vector<bool>& visited){
    
    if(visited[root] == true){
        return 0;
    }
    
    if(edges[root].size() == 1){
        totSums[root] = vals[root];
        visited[root] = true;
        return vals[root];
    }
    
    vector<int> children = edges[root];
    int totalSum = 0;
    visited[root] = true;
    for(int i = 0;i < children.size();i++){
        int child = children[i];
        totalSum += dfs(child,
                       edges,
                       totSums,
                       vals,
                       visited);
    }
    totalSum += vals[root];
    totSums[root] = totalSum;
    
    return totalSum;
    
}


int main(){
    
    /* Parsing the input */
    int n;
    cin>>n;
    
    vector<int> vals(n + 1);
    for(int i = 1;i <= n;i++){
        int temp;
        cin>>temp;
        vals[i] = temp;
    }
    
    vector<vector<int> > edges(n + 1);
    for(int i = 1;i <= n-1;i++){
        int node1,node2;
        cin>>node1>>node2;
        edges[node1].push_back(node2);
        edges[node2].push_back(node1);
    }
    /* Initializing the root. We initialize the element with max collections
     * as the root to decrease the depth of recursion */
    int maxLen = 0;
    int root;
    for(int i = 1;i <= n;i++){
        if(edges[i].size() > maxLen){
            maxLen = edges[i].size();
            root = i;    
        }
    }
    
    /* Performing DFS to compute an array of totSums. These indicate sum of all 
     * values of the tree rooted at the specific node. Including value of node */
    vector<int> totSums(n+1);
    vector<bool> visited(n+1);
    for(int i = 1;i <= n;i++){
        totSums[i] = 0;
        visited[i] = false;
    }
    // DFS returns the total sum rooted at tree
    int s = dfs(root,edges,totSums,vals,visited);
    
    
    int minDiff;
    int count = 0;
    for(int i = 1;i <= n ;i++){
        if(i != root){
            if(count == 0){
                minDiff = abs(s - 2*totSums[i]);
                count++;
            }else{
                int curDiff = abs(s - 2*totSums[i]);
                if(curDiff < minDiff)
                    minDiff = curDiff;
            }
        }
    }
    
    cout<<minDiff<<endl;
    return 0;
}
