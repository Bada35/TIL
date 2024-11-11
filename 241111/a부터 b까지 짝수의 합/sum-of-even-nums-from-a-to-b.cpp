#include <iostream>
using namespace std;

int main() {
    int a, b, sum_val = 0;
    cin >> a >> b;

    if (a % 2) a++;

    for (int i = a; i <= b; i += 2) sum_val += i;

    cout << sum_val;
    
    return 0;
}