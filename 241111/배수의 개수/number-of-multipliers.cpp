#include <iostream>
using namespace std;

int main() {
    int num, cnt_3 = 0, cnt_5 = 0;

    for (int i = 0; i < 10; i++) {
        cin >> num;
        if (num % 3 == 0) cnt_3++;
        if(num % 5 == 0) cnt_5++;
    }

    cout << cnt_3 << " " << cnt_5 << endl;

    return 0;
}