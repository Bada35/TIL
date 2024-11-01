#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, cnt = 0;

    cin >> n;

    for(int i = 1; i <= n; i++) {
        if (!(i % 2)){
            continue;
        }
        else if (!(i % 3)) {
            continue;
        }
        else if (!(i % 5)) {
            continue;
        }
        cnt++;
    }

    cout << cnt;
    return 0;
}