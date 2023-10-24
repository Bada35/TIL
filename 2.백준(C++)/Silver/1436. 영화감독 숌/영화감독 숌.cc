#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    int cnt = 0;
    int num = 665;

    while (true) {
        num += 1;
        if (to_string(num).find("666") != string::npos) {
            cnt += 1;
        }

        if (cnt == N) {
            cout << num << endl;
            break;
        }
    }

    return 0;
}
