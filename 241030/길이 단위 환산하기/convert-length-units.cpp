#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    const double FT_TO_CM = 30.48;
    double n;

    cin >> n;

    cout << fixed;
    cout.precision(1);

    cout << n * FT_TO_CM;

    return 0;
}