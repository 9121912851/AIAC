
    #include <iostream>

    int factorial_cpp(int n);

    int main() {
        int inputs[] = {5, 0};
        for (int inp : inputs) {
            std::cout << "Input: " << inp << " -> Output: Factorial = " << factorial_cpp(inp) << std::endl;
        }
        return 0;
    }

    int factorial_cpp(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial_cpp(n - 1);
    }
    