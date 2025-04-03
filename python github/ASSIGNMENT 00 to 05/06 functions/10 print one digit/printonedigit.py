def print_ones_digit(num):
    # Get the ones digit by using the modulo operator
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompt the user for input
    num = int(input("Enter a number: "))
    
    # Call the print_ones_digit function
    print_ones_digit(num)

# Call main to run the program
if __name__ == "__main__":
    main()
