def convert_temperature():
    temp = input("Enter the temperature value: ")
    if temp.replace('.', '', 1).isdigit():
        temp = float(temp)
        unit = input("Enter the unit (C/F): ").upper()
        if unit == 'C':
            print(f"{temp}°C = {(temp * 9/5) + 32:.2f}°F")
        elif unit == 'F':
            print(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        else:
            print("Invalid unit! Use 'C' or 'F'.")
    else:
        print("Please enter a valid number.")
convert_temperature()