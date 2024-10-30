#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string s, t, temp;

    cin >> s >> t;

    temp = s;
    s = t;
    t = temp;

    cout << s << "\n" << t;
    
    return 0;
}