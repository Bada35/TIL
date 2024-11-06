#include <iostream>
using namespace std;

int main() {
    int age, res = 0;
    char gender;

    cin >> age >> gender;

    if (age >= 19 && gender == 'M') {
        res = 1;
    }
    else {
        cin >> age >> gender;
        if (age >= 19 && gender == 'M') {
        res = 1;
        }
    }

    cout << res;
    
    return 0;
}