#include <iostream>
using namespace std;

int main() {
    int a, b, temp, sum_val = 0;
    cin >> a >> b;

    if (a > b) swap(a, b);

    if (a % 5 != 0) a = a + (5 - a % 5);

    for (int i = a; i <= b; i += 5) sum_val += i;

    cout << sum_val;

    return 0;
}