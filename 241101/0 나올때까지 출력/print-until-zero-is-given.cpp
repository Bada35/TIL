#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a;

    while(true) {
        cin >> a;
        if (a) {
            cout << a << endl;
            continue;
        }
        else {
            break;
        }
    }
    return 0;
}