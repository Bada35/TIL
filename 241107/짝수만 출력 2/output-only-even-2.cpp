#include <iostream>
using namespace std;

int main() {
    int b, a;
    cin >> b >> a;

    if (b % 2) b--;

    while (b >= a) {
        cout << b << " ";
        b -= 2;
    }
    
    return 0;
}