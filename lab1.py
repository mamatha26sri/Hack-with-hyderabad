def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32)*5.0/9.0
def celsius_to_fahrenheit(celsius):
  return (celsius*9.0/5.0)+32
def main():
  while True:
   print("\nTemperature Conversion Memu:")
   print("1.Convert Fahrenheit to Celsius")
   print("2.Convert Celsius to Fahrenheit")
   print("3.Exit")
   choice = input("Enter your choice(1/2/3):")
   if choice == '1':
       f = float(input("Enter temperature in Fahrenheit:"))
       c = fahrenheit_to_celsius(f)
        print(f"{f:2f}°F is equal to {c:.2f}°C")
    elif choice == '2':
       c = float(input("Enter temperature in Celsius:"))
       f = celsius_to_fahrenheit(C)
        print(f"{c:.2f}°C is equal to {f:.2f}°F")
    elif choice == '3':
        print("Exiting program. Goodbye!")
       break
        print("Invalid choice: Please enter 1,2, or 3.")

if __name__ == '__main__':
   main()
