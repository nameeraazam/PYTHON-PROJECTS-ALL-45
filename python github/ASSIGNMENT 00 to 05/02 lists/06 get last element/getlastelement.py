
def get_last_element(lst):
    """Prints the last element of the provided list."""
    print(lst[-1])  # Accesses the last element directly using negative indexing

def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    while True:
        elem = input("Please enter an element of the list or press Enter to stop: ")
        if elem == "":  # Stop if user presses Enter without typing anything
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    get_last_element(lst)  # Print the last element in the list

if __name__ == '__main__':  # Correct check for main execution
    main()
