/*Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are  lines of numeric input:
The first line has a double, meal_cost (the cost of the meal before tax and tip).
The second line has an integer, tip_percent (the percentage of meal_cost being added as tip).
The third line has an integer, tax_percent (the percentage of meal_cost being added as tax).

Output Format

Print the total meal cost, where total_cost is the rounded integer result of the entire bill (meal_cost with added tax and tip).*/

#include <bits/stdc++.h>

using namespace std;

// Complete the solve function below.
void solve(double meal_cost, int tip_percent, int tax_percent) {
    double total_cost = 0;

    total_cost = meal_cost + meal_cost*tip_percent/100 + meal_cost*tax_percent/100;

    cout << round(total_cost);

}

int main()
{
    double meal_cost;
    cin >> meal_cost;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int tip_percent;
    cin >> tip_percent;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int tax_percent;
    cin >> tax_percent;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    solve(meal_cost, tip_percent, tax_percent);

    return 0;
}
