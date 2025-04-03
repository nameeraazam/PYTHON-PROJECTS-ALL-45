# Step 1: Define the dictionary with fruit names and prices
fruit_prices = {
    "apple": 1.5,
    "durian": 5.0,
    "jackfruit": 3.0,
    "kiwi": 2.0,
    "rambutan": 4.0,
    "mango": 2.5
}

# Step 2: Initialize a variable to store the total cost
total_cost = 0

# Step 3: Loop through the dictionary and prompt the user for the quantity of each fruit
for fruit, price in fruit_prices.items():
    # Ask the user how many of this fruit they want
    quantity = int(input(f"How many ({fruit}) do you want?: "))
    
    # Step 4: Add the cost of this fruit to the total cost
    total_cost += quantity * price

# Step 5: Print the total cost
print(f"Your total is ${total_cost:.2f}")
