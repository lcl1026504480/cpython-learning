/*
* @Author: lcl1026504480
* @Date:   2019-06-17 15:05:19
* @Last Modified by:   lcl1026504480
* @Last Modified time: 2019-06-17 15:07:15
*/

#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{
    /* code */
    std::vector<int> v(1);
    v[0]=1;
    v.push_back(1);
    cout<<v.size();
    return 0;
}