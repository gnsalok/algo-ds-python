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

<<<<<<< HEAD
    for(int i=0; i<arr.size(); i++){
        cout<< arr[i] <<", ";
    }

=======
>>>>>>> c75dfc4c416c5808834cc2ebc42a362547518479
    return 0;
}