#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    for (int i = a; i <= b; i % 2 == 1 ? i *= 2 : i += 3) {
        cout << i << " ";
    }

    return 0;
}