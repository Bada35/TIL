#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int N, cnt = 0;

    cin >> N;

    while(N != 1) {
        if (N % 2) {
            N = N * 3 + 1;
            cnt ++;
        }
        else {
            N /= 2;
            cnt ++;
        }
    }

    cout << cnt;

    return 0;
}