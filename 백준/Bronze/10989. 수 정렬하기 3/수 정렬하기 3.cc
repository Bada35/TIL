#include<iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	//freopen_s(new FILE*, "input.txt", "r", stdin);

	int N;
	cin >> N;

	int nums[10001] = { 0 };

	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		nums[tmp]++;
	}

	for (int i = 1; i < 10001; i++) {
		for (int j = 0; j < nums[i]; j++) {
			cout << i << '\n';
		}
	}

}