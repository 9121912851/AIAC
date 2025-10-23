# ...existing code...
from pathlib import Path
import subprocess
import shutil

def print_numbers():
    """Print the first 10 natural numbers (1..10) using a loop."""
    for n in range(1, 11):
        print(n)

# JavaScript companion code (will be written to task1.js and executed with node if available)
JS_CODE = """function printNumbers() {
  // Print the first 10 natural numbers (1..10)
  for (let i = 1; i <= 10; i++) {
    console.log(i);
  }
}
printNumbers();
"""

if __name__ == "__main__":
    # Call the Python function
    print("Python output:")
    print_numbers()

    # Write JS file next to this Python file
    js_path = Path(__file__).with_suffix('.js')
    js_path.write_text(JS_CODE, encoding='utf-8')

    # Attempt to run the JS with node
    print("\nJavaScript output (via node):")
    if shutil.which("node"):
        subprocess.run(["node", str(js_path)])
    else:
        print(f"Node not found. JS file written to: {js_path}")
# ...existing code...
