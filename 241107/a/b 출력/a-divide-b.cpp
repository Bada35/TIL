#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    cout << a / b << ".";

    int remainder = a % b;

    for (int i = 0; i < 20; i++) {
        remainder *= 10;                // 나머지에 10을 곱하여 다음 자리로 이동
        int digit = remainder / b;      // 현재 자릿수 계산
        cout << digit;                  // 자릿수 출력
        remainder %= b;                 // 새로운 나머지 계산
    }

    cout << endl;
    return 0;
}