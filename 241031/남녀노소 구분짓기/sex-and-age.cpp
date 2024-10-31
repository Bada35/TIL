#include <iostream>
using namespace std;

int main() {
    int gender, age;
    cin >> gender >> age;

    cout << (gender ? (age > 18 ? "WOMAN" : "GIRL") : (age > 18 ? "MAN" : "BOY"));
    
    return 0;
}