#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char n;

    cin >> n;

    if(n == 'S'){
        cout << "Superior";
    }
    else if (n == 'A'){
        cout << "Excellent";
    }
    else if (n == 'B'){
        cout << "Good";
    }
    else if (n == 'C'){
        cout << "Usually";
    }
    else if (n == 'D'){
        cout << "Effort";
    }
    else{
        cout << "Failure";
    }
    return 0;
}