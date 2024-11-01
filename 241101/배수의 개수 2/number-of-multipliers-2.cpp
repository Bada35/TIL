#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int cnt = 0, num;

    for(int i = 0; i < 10; i++){
        cin >> num;
        if (num % 2) {
        cnt ++;
    }
    }

    cout << cnt;

    return 0;
}