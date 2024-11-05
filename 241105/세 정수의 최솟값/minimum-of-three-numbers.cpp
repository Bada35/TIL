#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c;
    int res;

    cin >> a >> b >> c;
    res = a;

    if(b <= res){
        res = b;
    }

    cout << (c <= res ? c : res);

    return 0;
}