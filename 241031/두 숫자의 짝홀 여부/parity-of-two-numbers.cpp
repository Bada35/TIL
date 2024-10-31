#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;

    cin >> a >> b;

    if (a % 2){
        cout << "odd";
    } else{
        cout << "even";
    }
    
    cout << endl;

    if (b % 2){
        cout << "odd";
    } else {
        cout << "even";
    }
    return 0;
}