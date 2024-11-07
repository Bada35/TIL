#include <iostream>
using namespace std;

int main() {
    int a, b, temp;
    cin >> a >> b;

    if (b < a) {
        temp = b;
        b = a;
        a = temp;
    }

    for (int i = b; i >= a; --i) {
        cout << i << " ";
    }

    return 0;
}