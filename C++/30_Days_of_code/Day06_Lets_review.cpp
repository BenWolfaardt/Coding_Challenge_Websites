/*Task
Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample 
below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S.

Constraints

1 <= T <= 10
2 <= length of S <= 10000

Output Format

For each String Sj (where 0 <= j <= T - 1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    string s;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i = 0; i < t; i++){
        cin >> s;

        for (int j1 = 0; j1 < s.length(); (j1+=2)){
            cout << s[j1];
        }
        cout << " ";
        for (int j2 = 1; j2 < s.length(); j2+=2){
            cout << s[j2];
        }
        cout << '\n';
    }
    return 0;
}
