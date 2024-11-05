#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    
    cin >> n;

    cout << (n >= 90 ? "A" : (n >= 80 ? "B" : (n >= 70 ? "C" : (n >= 60 ? "D" : "F"))));
    
    return 0;
}