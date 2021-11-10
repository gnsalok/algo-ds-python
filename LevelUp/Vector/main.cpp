#include<iostream>
#include<vector>
using namespace std;

int main(){

    vector<int> arr = {1,2,3,4,5};

    cout<<arr.size() <<endl;

    cout<<arr.capacity() <<endl;

    return 0;
}