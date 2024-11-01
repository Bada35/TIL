#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    char res = 'N';

    cin >> n;

    for(int i = 2; i < n; i++) {
        if (!(n % i)) {
            res = 'C';
            break;
        }
    }

    cout << res;

    return 0;
}