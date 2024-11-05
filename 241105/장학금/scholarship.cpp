#include <iostream>
using namespace std;

int main() {
    int mid, fin;
    cin >> mid >> fin;

    int scholarship = 0;

    if(mid >= 90){
        if (fin >= 95){
            scholarship = 100000;
        }
        else if (fin >= 90){
            scholarship = 50000;
        }
    }

    cout << scholarship;

    return 0;
}