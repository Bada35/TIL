#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<pair<int, int>> person;

	for (int i = 0; i < N; i++) {
		int w, h;
		cin >> w >> h;
		person.push_back(make_pair(w, h));
	}

	for (int i = 0; i < N; i++) {
		int cnt = 1;
		for (int j = 0; j < N; j++) {
			if (person[j].first > person[i].first and person[j].second > person[i].second) {
				cnt++;
			}
		}
		cout << cnt << " ";
	}

}