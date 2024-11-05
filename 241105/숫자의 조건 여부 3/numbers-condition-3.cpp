#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;

    cout << (!(a % 13) || !(a % 19) ? "True" : "False");
    
    return 0;
}