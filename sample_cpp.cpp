// This is a sample file.

#include <iostream>
#include <fstream>
#include <vector>
#include <random>

int main() {
	std::mt19937 generate(0);
	std::normal_distribution<> randnorm(100, 15);

	int n = 100;
	std::vector<double> x(n), y(n);
	for (int i = 0; i < n; ++i) {
		x[i] = randnorm(generate);
		y[i] = randnorm(generate);
	}

	std::ofstream output("sample_cpp_output.csv");
	output << "i,x,y" << std::endl;
	for (int i = 0; i < n; ++i) {
		output << i + 1 << "," << x[i] << "," << y[i] << std::endl;
	}
	output.close();

	return 0;
}