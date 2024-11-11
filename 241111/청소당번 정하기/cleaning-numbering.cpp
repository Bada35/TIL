#include <iostream>
using namespace std;

int main() {
    int n, classroom = 0, hallway = 0, toilet = 0;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i % 12 == 0) toilet++;
        else if (i % 3 == 0) hallway++;
        else if (i % 2 == 0) classroom++;
    }

    cout << classroom << " " << hallway << " " << toilet;

    return 0;
}