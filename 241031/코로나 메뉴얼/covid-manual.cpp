#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char sym;
    int degree, cnt = 0;

    for (int i = 0; i < 3; i++) {
        cin >> sym >> degree;
        if ((sym == 'Y') && (degree >= 37)) {
            cnt ++;
        }
    }

    if (cnt >= 2){
        cout << "E";
    }
    else {
        cout << "N";
    }


    return 0;
}