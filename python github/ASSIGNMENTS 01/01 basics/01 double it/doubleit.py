def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))
    
    # Loop while the current value is less than 100
    while curr_value < 100:
        # Double the current value
        curr_value *= 2
        
        # Print the doubled value
        print(curr_value, end=" ")

# Call the main function to run the program
if __name__ == "__main__":
    main()
