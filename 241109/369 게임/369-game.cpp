#include <iostream>
using namespace std;

int main() {
    int n, upper, lower;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        upper = (i / 10 == 0 ? 1 : i / 10);
        lower = (i % 10 == 0 ? 1 : i % 10);

        if ((upper * lower * i) % 3 == 0) cout << 0 << " ";
        else cout << i << " ";
    }
    return 0;
}