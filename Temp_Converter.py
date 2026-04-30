def temp_converter(choice, value):
    if choice == "1":
        result = (value * 9/5) + 32
        return f"{result} °F"

    elif choice == "2":
        result = (value - 32) * 5/9
        return f"{result} °C"

    else:
        return "Invalid choice!"


# Take input
conversion_type = input("Enter conversion \n1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius\nChoice: ")
temperature = float(input("Enter temperature value: "))

# Call function
result = temp_converter(conversion_type, temperature)

# Output
print("Result:", result)