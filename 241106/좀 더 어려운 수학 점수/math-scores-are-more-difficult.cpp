#include <iostream>
using namespace std;

int main() {
    int math_A, math_B, eng_A, eng_B;
    char res = 'A';
    cin >> math_A >> eng_A >> math_B >> eng_B;

    if (math_A < math_B) {
        res = 'B';
    }
    else if (math_A == math_B) {
        if (eng_A < eng_B) {
            res = 'B';
        }
    }

    cout << res;
    
    return 0;
}