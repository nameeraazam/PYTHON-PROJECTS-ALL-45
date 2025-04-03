def get_user_info():
    # Ask for the user's first name and store it
    first_name = input("What is your first name?: ")
    
    # Ask for the user's last name and store it
    last_name = input("What is your last name?: ")
    
    # Ask for the user's email address and store it
    email_address = input("What is your email address?: ")
    
    # Return the collected information as a tuple
    return first_name, last_name, email_address

def main():
    # Call get_user_info and store the returned tuple
    user_data = get_user_info()
    
    # Print the received user data
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
