#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define MIN(a,b) (a<b?a:b)

struct table{
    int distance,cost,grade;
    int flood;
    bool operator < (const table& str) const
    {
        return (distance < str.distance);
    }
};
void calc_grade(vector<table> &tables,int index){
    int n;
    int flood,cost,distance;
    int grade;
    n = tables.size();
    if (index != n-1){
        flood = 1+tables[index+1].flood;
        cost = tables[index+1].cost;
        distance =  tables[index+1].distance-tables[index].distance;
        grade = tables[index+1].grade;
    }else{
        flood = 1;
        cost = 0;
        distance = 0;
        grade = 0;
    }
    tables[index].grade = grade + (flood - 1)*distance;
    if(index == 0||(tables[index].cost<=flood*(tables[index].distance - tables[index-1].distance))){
        tables[index].flood = 0;
        tables[index].grade += tables[index].cost;
    }else{
        tables[index].flood = flood;
    }
    //cout<< tables[index].grade<<"____"<<tables[index].flood<<endl;
}
int main(){
    int n;
    cin >> n;
    vector<table> tables(n);
    for(int i=0;i<n;i++){
        cin >> tables[i].distance;
    }
    for(int i=0;i<n;i++){
        cin >> tables[i].cost;
    }
    sort(tables.begin(),tables.end());
    for(int i=n-1;i>=0;i--){
        calc_grade(tables,i);
    }
    cout<<tables[0].grade<<endl;
}
