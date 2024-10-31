#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char sym[3];
    int degree[3], cnt = 0;

    for (int i = 0; i < 3; i++) {
        cin >> sym[i] >> degree[i];
        if ((sym[i] == 'Y') && (degree[i] >= 37)) {
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