#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int res;
    if ((a >= b && a <= c) || (a >= c && a <= b)) {
        res = a;
    } else if ((b >= a && b <= c) || (b >= c && b <= a)) {
        res = b;
    } else {
        res = c;
    }

    cout << res;

    return 0;
}