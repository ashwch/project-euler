"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=14
lang: c++
"""
#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    unsigned long long int i,count,maxx,j,ans;
    maxx=0;
    for(i=2;i<=1000000;i++){
        j=i;
        count=0;
        while (j!=1){
            if (j%2==0){j/=2;}
            else {j=3*j+1;}
            count++;
        }
        if (count>maxx){
            maxx=count;
            ans=i;
        }
        
        
     }
    cout <<ans<<"->" <<maxx<<endl;

}
