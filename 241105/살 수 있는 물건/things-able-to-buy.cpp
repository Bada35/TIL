#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;

    cout << (n >= 3000 ? "book" : (n >= 1000 ? "mask" : "no"));

    return 0;
}