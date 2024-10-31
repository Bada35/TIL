#include <iostream>
using namespace std;

int main() {
    char sym;
    int degree, cnt = 0;

    for (int i = 0; i < 3; i++) {
        cin >> sym >> degree;
        if ((sym == 'Y') && (degree >= 37)) {
            cnt++;
        }
    }

    cout << (cnt >= 2 ? "E" : "N");

    return 0;
}