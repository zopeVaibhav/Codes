#include <bits/stdc++.h>
using namespace std;
 
int main () {
    
    int arr[]={1,2,3,4,5,6,7,8,9,10};
    int target = 10;
    for (int i=0; i<sizeof(arr)/sizeof(arr[0]); i++){
        if(arr[i] == target){
            cout << "found" << endl;
        }
    }

    int size = sizeof(arr)/sizeof(arr[0]);

    int s = 0;
    int e = size-1;
    int mid = s +(e-s)/2;

    while (s<=e){
        if(arr[mid] == target){
            cout << "found" << endl;
            break;
        }
        else if(arr[mid] > target){
            e = mid-1;
        }
        else {
            s = mid+1;
        }
    mid = s +(e-s)/2;
    }



    return 0;
}