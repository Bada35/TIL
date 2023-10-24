#include <iostream>
#include <iomanip>

int main(void)
{
	// freopen_s(new FILE*, "input.txt", "r", stdin);
	double A, B;

	std::cin >> A >> B;
	std::cout << std::setprecision(10) << A / B;

	return 0;
}
