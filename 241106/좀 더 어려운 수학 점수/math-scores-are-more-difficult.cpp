#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    if(A > B){
        cout << "A";
    }
    else if(A < B){
        cout << "B";
    }
    else{
        cin >> A >> B;
        if(A > B){
        cout << "A";
    }
    else if(A < B){
        cout << "B";
    }
    }
    return 0;
}