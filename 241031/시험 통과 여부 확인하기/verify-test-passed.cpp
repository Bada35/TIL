#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;

    cin >> n;

    if (n >= 80){
        cout << "pass";
    } else{
        cout << 80 - n << " more socre";
    }
    return 0;
}