#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    cout << a / b << ".";

    int remainder = a % b;

    for (int i = 0; i < 20; i++) {
        remainder *= 10;
        int digit = remainder / b;
        cout << digit;
        remainder %= b;
    }

    cout << endl;
    return 0;
}