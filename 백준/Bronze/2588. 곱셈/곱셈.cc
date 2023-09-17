#include <iostream>

int main() {
	int A, B;
	std::cin >> A >> B;
	std::cout << A * (B % 10) << "\n" << A * (B / 10 % 10) << "\n" << A * (B / 100) << "\n" << A * B;
}