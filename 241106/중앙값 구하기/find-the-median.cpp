#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int res = a;

    if(a > b && a > c){
        if(b > c) res = b;
        else res = c;
    }
    else if (a < b && a < c){
        if (b < c) res = b;
        else res = c;
    }

    cout << res;

    return 0;
}