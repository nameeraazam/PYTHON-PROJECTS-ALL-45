
# Mars Weight Calculation Program

# Prompt the user to input their weight on Earth
earth_weight = float(input("Enter your weight on Earth: "))

# Calculate the equivalent weight on Mars (37.8% of Earth's weight)
mars_weight = earth_weight * 0.378

# Round the result to two decimal places
mars_weight_rounded = round(mars_weight, 2)

# Output the calculated weight on Mars
print(f"The equivalent weight on Mars is: {mars_weight_rounded}")
