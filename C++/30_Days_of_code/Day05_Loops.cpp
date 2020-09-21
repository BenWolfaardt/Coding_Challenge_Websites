/*Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Task
Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.

Input Format
A single integer, n.

Constraints
2 <= n <=20*/

#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i = 1; i < 11; i++){
        cout << n << " x " << i << " = " << i*n << '\n';
    }

    return 0;
}
