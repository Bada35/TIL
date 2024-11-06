#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int res = a;

    if (b > res) res = b;
    if (c > res) res = c;
    
    cout << res;

    return 0;
}