#include<iostream>
// #include<bits/stdc++.h>
using namespace std;

int main()
{
    pair<int,int> p[3];
    p[3]=make_pair(12,21);
    cout<<p[3].first<<p[3].second;
    int i;
    i=0;
    while (i<3)
    {
        p[i]=make_pair(i+2,i*2);i++;
        cout<<p[i].first<<" "<<p[i].second;
    }
    return 0;
}