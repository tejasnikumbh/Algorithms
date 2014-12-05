#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

/* ============================================================== *
 * Creates a String with n1 5s followed by n2 3s                  *
 * ============================================================== */
string createStr(int n1,int n2){
    if(n1<0 || n2<0) return "-1";
    string num = "";
    for(int i = 0;i < n1;i++)
        num += "5";
    for(int i = 0;i < n2;i++)
        num += "3";
    return num;
}


/* ============================================================== *
 * Returns the maximum of int values of 2 strings n1 and n2       *
 * ============================================================== */
string getMax(string n1,string n2){
    stringstream s1(n1);
    stringstream s2(n2);
    int n1Num,n2Num;
    s1>>n1Num;
    s2>>n2Num;
    if(n1Num>n2Num) return n1;
    else return n2;
}


/* ============================================================== *
 * Main function to run the program                               *
 * ============================================================== */
int main() {
    int t;
    cin>>t;
    
    int N;
    for(int i = 0;i < t;i++){
        cin>>N;
        string num = "";
        // Three cases considered . Greedy approach applied wherein
        // the number of 5s in MSB positions is maximized
        if(N % 3 == 0){
            num = createStr(N,0);
        }else if(N % 3 == 1){
            num = createStr(N-10,10);        
            if(num == "-1" && N % 5 == 0)
                num = createStr(0,N);
        }else{
            num = createStr(N-5,5);        
            if(num == "-1" && N % 5 == 0)
                num = createStr(0,N);
        }
       cout<<num<<endl;
    }
    return 0;
}
