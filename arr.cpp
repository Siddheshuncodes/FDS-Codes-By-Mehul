#include<iostream>
using namespace std;

int main(){

    int a[5],i,j,k,val; 

    for(i=0;i<5;i++){

        cout<<"Enter the the "<<i<<" value: ";
        cin>>a[i];
    }

    cout<<"Enter the value to search: ";
    cin>>val;

     for(k=0;k<5;k++){

        if(a[k]==val){

            cout<<"Value is present at index number: "<<k;
        }
    }

    for(j=0;j<5;j++){

        cout<<"\nThe "<<j<<" value is: "<<a[j];
        
    }

    return 0;
}