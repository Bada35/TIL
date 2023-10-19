#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main() {
	string A, B;
	cin >> A >> B;

	int numA = stoi(string(A.rbegin(), A.rend()));
	int numB = stoi(string(B.rbegin(), B.rend()));

	int res = max(numA, numB);

	cout << res << '\n';

	return 0;

}