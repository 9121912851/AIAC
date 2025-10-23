from pathlib import Path
import subprocess
import shutil
import os

# -------------------------------
# 1️⃣  Print Numbers in Python
# -------------------------------
def print_numbers():
    """Print the first 10 natural numbers (1..10) using a loop."""
    for n in range(1, 11):
        print(n)

# JavaScript companion code
JS_CODE = """function printNumbers() {
  for (let i = 1; i <= 10; i++) {
    console.log(i);
  }
}
printNumbers();
"""

# -------------------------------
# 2️⃣  Factorial in Python
# -------------------------------
def factorial_py(n):
    """Compute factorial recursively in Python."""
    if n == 0:
        return 1
    return n * factorial_py(n - 1)

# -------------------------------
# 3️⃣  Factorial in C++
# -------------------------------
CPP_CODE = """
#include <iostream>

int factorial_cpp(int n);

int main() {
    int inputs[] = {5, 0};
    for (int inp : inputs) {
        std::cout << "Input: " << inp << " -> Output: Factorial = " 
                  << factorial_cpp(inp) << std::endl;
    }
    return 0;
}

int factorial_cpp(int n) {
    if (n == 0)
        return 1;
    return n * factorial_cpp(n - 1);
}
"""

# -------------------------------
# 4️⃣  Main Runner
# -------------------------------
if __name__ == "__main__":
    # --- Python Numbers ---
    print("Python: print_numbers() output:")
    print_numbers()

    # --- JavaScript Numbers ---
    print("\nJavaScript: printNumbers() output:")
    js_path = Path(__file__).with_suffix('.js')
    js_path.write_text(JS_CODE, encoding='utf-8')
    if shutil.which("node"):
        subprocess.run(["node", str(js_path)])
    else:
        print(f"Node not found. JS file written to: {js_path}")

    # --- Python Factorials ---
    print("\nPython: factorial_py() output:")
    for inp in (5, 0):
        print(f"Input: {inp} -> Output: Factorial = {factorial_py(inp)}")

    # --- C++ Factorials ---
    print("\nC++: factorial_cpp() output:")
    cpp_path = Path("temp_factorial.cpp")
    cpp_path.write_text(CPP_CODE, encoding="utf-8")

    try:
        # Compile and execute
        subprocess.run(["g++", str(cpp_path), "-o", "temp_factorial"], check=True, capture_output=True)
        result = subprocess.run(["./temp_factorial"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing C++ code:\n{e.stderr}")

    # --- Optional cleanup ---
    if Path("temp_factorial").exists():
        os.remove("temp_factorial")
    if cpp_path.exists():
        os.remove(cpp_path)
