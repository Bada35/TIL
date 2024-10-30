#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    const double fit_ratio = 30.48;
    const int mi_ratio = 160934;

    cout << fixed;
    cout.precision(1);

    cout << "9.2ft = " << 9.2 * fit_ratio << "cm\n1.3mi = " << 1.3 * mi_ratio << "cm";

    return 0;
}