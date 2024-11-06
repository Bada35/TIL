#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int max_val = max(a, max(b, c));
    int min_val = min(a, min(b, c));
    
    // 중앙값은 전체 값 중에서 최대값과 최소값이 아닌 값
    int res = a + b + c - max_val - min_val;

    cout << res;

    return 0;
}