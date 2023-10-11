#include <iostream>

using namespace std;

int main() {

	int N, res = -1;
	cin >> N;

	for (int i = N / 5; i >= 0; --i) {
		if ((N - 5 * i) % 3 == 0) {
			res = i + (N - 5 * i) / 3;
			break;
		}
	}

	cout << res;
	
}