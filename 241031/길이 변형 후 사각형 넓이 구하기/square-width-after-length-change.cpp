#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int width, height;

    cin >> width >> height;

    width += 8;
    height *= 3;

    cout << width << "\n" << height << "\n" << width * height;
    return 0;
}