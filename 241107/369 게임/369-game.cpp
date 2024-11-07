#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int tens = 1, units; // 십의자리, 일의자리

    for (int i = 1; i <= n; ++i) {
        tens = i / 10;
        units = i % 10;

        if ((i % 3 == 0) || (tens % 3 == 0) || (units % 3 == 0)) {
            cout << 0 << " ";
        }
        else cout << i;
    }

    return 0;
}