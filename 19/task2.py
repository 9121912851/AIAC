from pathlib import Path
import subprocess
import shutil

def print_numbers():
    """Print the first 10 natural numbers (1..10) using a loop."""
    for n in range(1, 11):
        print(n)

def check_number(num):
    """Return 'positive', 'negative', or 'zero' for the given number."""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

# Java companion code
JAVA_CODE = """public class CheckNumber {
  public static String checkNumber(int num) {
    if (num > 0) return "positive";
    else if (num < 0) return "negative";
    else return "zero";
  }

  public static void main(String[] args) {
    int[] tests = { -5, 0, 7 };
    for (int n : tests) {
      System.out.println(n + " -> " + checkNumber(n));
    }
  }
}
"""

# JavaScript companion code
JS_CODE = """function printNumbers() {
  // Print the first 10 natural numbers (1..10)
  for (let i = 1; i <= 10; i++) {
    console.log(i);
  }
}
printNumbers();
"""

if __name__ == "__main__":
    print("Python print_numbers output:")
    print_numbers()

    tests = [-5, 0, 7]
    print("\nPython check_number results:")
    py_results = []
    for n in tests:
        r = check_number(n)
        py_results.append(r)
        print(f"{n} -> {r}")

    # Write and run JS file
    js_path = Path(__file__).with_suffix('.js')
    js_path.write_text(JS_CODE, encoding='utf-8')
    print("\nJavaScript output (via node):")
    if shutil.which("node"):
        subprocess.run(["node", str(js_path)])
    else:
        print(f"Node not found. JS file written to: {js_path}")

    # Write Java file and compile/run
    java_path = Path(__file__).with_name("CheckNumber.java")
    java_path.write_text(JAVA_CODE, encoding='utf-8')
    print("\nJava output (via javac/java):")
    if shutil.which("javac") and shutil.which("java"):
        compile_proc = subprocess.run(["javac", str(java_path)], capture_output=True, text=True)
        if compile_proc.returncode != 0:
            print("javac failed:\n", compile_proc.stderr)
        else:
            run_proc = subprocess.run(["java", "-cp", str(java_path.parent), "CheckNumber"], capture_output=True, text=True)
            if run_proc.returncode != 0:
                print("java failed:\n", run_proc.stderr)
            else:
                java_out = run_proc.stdout.strip().splitlines()
                for i, line in enumerate(java_out):
                    print(line)
                print("\nComparing Python vs Java results:")
                for i, n in enumerate(tests):
                    parts = java_out[i].split("->")
                    java_result = parts[1].strip() if len(parts) > 1 else "<parse_error>"
                    match = "MATCH" if java_result == py_results[i] else "MISMATCH"
                    print(f"{n}: python={py_results[i]} java={java_result} => {match}")
    else:
        print(f"javac/java not found. Java file written to: {java_path}")
