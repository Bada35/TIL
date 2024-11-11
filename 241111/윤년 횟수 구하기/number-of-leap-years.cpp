#include <iostream>
using namespace std;

int main() {
    int n, cnt = 0;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        if ((i % 100 == 0) && (i % 400)) continue;
        else if (i % 4 == 0) cnt++;
    }

    cout << cnt;

    return 0;
}