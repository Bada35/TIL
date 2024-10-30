#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char c;
    double a, b;

    cin >> c >> a >> b;

    cout << fixed;
    cout.precision(2);
    cout << c << "\n" << a << "\n" << b;
    
    return 0;
}