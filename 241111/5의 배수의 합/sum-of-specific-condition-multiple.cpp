#include <iostream>
using namespace std;

int main() {
    int a, b, temp, sum_val = 0;
    cin >> a >> b;

    if (a > b) {
        temp = b;
        b = a;
        a = temp;
    }

    for (int i = a; i <= b; ++i) {
        if (i % 5 == 0) {
            sum_val += i;
        }
    }

    cout << sum_val;
    
    return 0;
}