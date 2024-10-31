#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int gender, age;

    cin >> gender >> age;

    if (gender) {
        if (age > 18){
            cout << "WOMAN";
        }
        else {
            cout << "GIRL";
        }
    }
    else{
        if (age > 18){
            cout << "MAN";
        }
        else {
            cout << "BOY";
        }
    }
    return 0;
}