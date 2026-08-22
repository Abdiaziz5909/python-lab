from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        val = float(input("Enter a number: "))
        
        sq_val = square(val)
        even_status = "Even" if is_even(int(val)) else "Odd"
        fah_val = celsius_to_fahrenheit(val)
        
        print(f"Square: {sq_val}")
        print(f"Number is: {even_status}")
        print(f"Fahrenheit equivalent: {fah_val:.2f}°F")
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()