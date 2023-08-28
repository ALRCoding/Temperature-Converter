import math

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5.0 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def main():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        f_temp = float(input("Enter temperature in Fahrenheit: "))
        c_temp = fahrenheit_to_celsius(f_temp)
        print(f"{f_temp}°F is equal to {c_temp:.2f}°C")
    elif choice == 2:
        c_temp = float(input("Enter temperature in Celsius: "))
        f_temp = celsius_to_fahrenheit(c_temp)
        print(f"{c_temp}°C is equal to {f_temp:.2f}°F")
    elif choice == 3:
        c_temp = float(input("Enter temperature in Celsius: "))
        k_temp = celsius_to_kelvin(c_temp)
        print(f"{c_temp}°C is equal to {k_temp:.2f} K")
    elif choice == 4:
        k_temp = float(input("Enter temperature in Kelvin: "))
        c_temp = kelvin_to_celsius(k_temp)
        print(f"{k_temp} K is equal to {c_temp:.2f}°C")
    elif choice == 5:
        f_temp = float(input("Enter temperature in Fahrenheit: "))
        k_temp = fahrenheit_to_kelvin(f_temp)
        print(f"{f_temp}°F is equal to {k_temp:.2f} K")
    elif choice == 6:
        k_temp = float(input("Enter temperature in Kelvin: "))
        f_temp = kelvin_to_fahrenheit(k_temp)
        print(f"{k_temp} K is equal to {f_temp:.2f}°F")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()