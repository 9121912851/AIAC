def convert_temperature():
    print("Enter the temperature value and units to convert (e.g., 100 F to C):")
    user_input = input().strip()
    # Expected format: "<value> <from_unit> to <to_unit>"
    try:
        parts = user_input.split()
        if len(parts) != 4 or parts[2].lower() != "to":
            print("Invalid format. Please use the format: <value> <from_unit> to <to_unit>")
            return
        value = float(parts[0])
        from_unit = parts[1].upper()
        to_unit = parts[3].upper()

        def f_to_c(f): return (f - 32) * 5 / 9
        def c_to_f(c): return c * 9 / 5 + 32
        def c_to_k(c): return c + 273.15
        def k_to_c(k): return k - 273.15
        def f_to_k(f): return (f - 32) * 5 / 9 + 273.15
        def k_to_f(k): return (k - 273.15) * 9 / 5 + 32

        if from_unit == to_unit:
            print(f"{value} {from_unit} is {value} {to_unit}")
        elif from_unit == "F" and to_unit == "C":
            result = f_to_c(value)
            print(f"{value} F is {result:.2f} C")
        elif from_unit == "C" and to_unit == "F":
            result = c_to_f(value)
            print(f"{value} C is {result:.2f} F")
        elif from_unit == "C" and to_unit == "K":
            result = c_to_k(value)
            print(f"{value} C is {result:.2f} K")
        elif from_unit == "K" and to_unit == "C":
            result = k_to_c(value)
            print(f"{value} K is {result:.2f} C")
        elif from_unit == "F" and to_unit == "K":
            result = f_to_k(value)
            print(f"{value} F is {result:.2f} K")
        elif from_unit == "K" and to_unit == "F":
            result = k_to_f(value)
            print(f"{value} K is {result:.2f} F")
        else:
            print("Unsupported unit conversion. Supported units: C, F, K.")
    except Exception as e:
        print("Error:", e)
        print("Please enter the input in the correct format.")

if __name__ == "__main__":
    convert_temperature()
