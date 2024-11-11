#include <iostream>
using namespace std;

int main() {
    int num, cnt = 0;

    for (int i = 0; i < 10; i++) {
        cin >> num;
        if (num % 2 == 1) {
            cnt ++;
        }
    }

    cout << cnt;

    return 0;
}