#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int num, cnt = 0, sum_val = 0;

    for (int i = 0; i < 10; ++i) {
        cin >> num;
        if (num >= 0 && num <= 200) {
            sum_val += num;
            cnt++;
        }
    }

    cout << sum_val << fixed << setprecision(1) << " " << (double)sum_val / cnt;
    
    return 0;
}