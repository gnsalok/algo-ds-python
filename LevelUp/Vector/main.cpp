#include<iostream>
#include<vector>
using namespace std;

int main(){

    //vector<int> arr = {1,2,3,4,5};

    vector<int> arr(10,8);

    arr.pop_back();

    arr.push_back(11);

    cout<<arr.size() <<endl;

    cout<<arr.capacity() <<endl;

    for(int i=0; i<arr.size(); i++){
        cout<< arr[i] <<", ";
    }

    return 0;
}