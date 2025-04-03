#Problem #1: List Practice
#Now practice writing code with lists! Implement the functionality described in the comments below.
#
#def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

#def main():
#    # Create a list called `fruit_list` that contains the following fruits:
#    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
#    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
#    
#    # Print the length of the list.
#    print(len(fruit_list))
#    
#    # Add 'mango' at the end of the list.
#    fruit_list.append('mango')
#    
#    # Print the updated list.
#    print(fruit_list)
#
#if __name__ == "__main__":
#    main()










#2: Index Game

def access_element(lst, index):
    """
    Access an element from the list at the specified index.
    Returns the element or an error message if index is out of range.
    """
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range. Valid indices are from {-len(lst)} to {len(lst) - 1}."

def modify_element(lst, index, new_value):
    """
    Modify an element in the list at the specified index.
    Returns the updated list or an error message if index is out of range.
    """
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return f"Error: Index {index} is out of range. Valid indices are from {-len(lst)} to {len(lst) - 1}."

def slice_list(lst, start_index, end_index):
    """
    Return a slice of the list from start_index up to (but not including) end_index.
    Handles out of range indices by adjusting them to valid values.
    """
    # Python's slicing is forgiving with out-of-range indices, but we'll provide feedback
    max_index = len(lst)
    
    # Adjust indices if needed
    if start_index < -max_index:
        print(f"Warning: Start index {start_index} is too small, adjusted to {-max_index}")
        start_index = -max_index
    elif start_index > max_index:
        print(f"Warning: Start index {start_index} is too large, adjusted to {max_index}")
        start_index = max_index
        
    if end_index < -max_index:
        print(f"Warning: End index {end_index} is too small, adjusted to {-max_index}")
        end_index = -max_index
    elif end_index > max_index:
        print(f"Warning: End index {end_index} is too large, adjusted to {max_index}")
        end_index = max_index
        
    return lst[start_index:end_index]

def display_list_with_indices(lst):
    """Display the list with indices for better visualization."""
    print("\nCurrent list:")
    print(f"List: {lst}")
    print("Positive indices:", end=" ")
    for i in range(len(lst)):
        print(f"{i}:{lst[i]}", end="  ")
    print("\nNegative indices:", end=" ")
    for i in range(-len(lst), 0):
        print(f"{i}:{lst[i]}", end="  ")
    print("\n")

def play_index_game():
    """
    Main function to play the index game.
    """
    # Initialize a list with different elements
    my_list = ["apple", 42, "banana", True, 3.14]
    
    print("Welcome to the Index Game!")
    print("This game will help you practice working with list indices in Python.")
    
    while True:
        display_list_with_indices(my_list)
        
        print("Select an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            try:
                index = int(input("Enter the index to access: "))
                result = access_element(my_list, index)
                print(f"Element at index {index} is: {result}")
            except ValueError:
                print("Please enter a valid integer for the index.")
                
        elif choice == "2":
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                
                # Try to convert new_value to appropriate type if it looks like a number
                if new_value.isdigit():
                    new_value = int(new_value)
                elif new_value.lower() == "true":
                    new_value = True
                elif new_value.lower() == "false":
                    new_value = False
                elif new_value.replace(".", "", 1).isdigit() and new_value.count(".") <= 1:
                    new_value = float(new_value)
                    
                result = modify_element(my_list, index, new_value)
                if isinstance(result, list):
                    print("Element modified successfully!")
                    my_list = result
                else:
                    print(result)  # Print error message
            except ValueError:
                print("Please enter a valid integer for the index.")
                
        elif choice == "3":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print(f"Sliced list [{start}:{end}] is: {result}")
            except ValueError:
                print("Please enter valid integers for the indices.")
                
        elif choice == "4":
            print("Thank you for playing the Index Game!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    play_index_game()