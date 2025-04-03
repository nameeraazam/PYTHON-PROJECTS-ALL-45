import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    # TODO: Write your code here!!! :)

if __name__ == "__main__":
    main()


    def main():
    # Dictionary containing the gravity percentages of planets
    planet_gravity = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }

    # Step 1: Ask the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Step 2: Ask the user for the name of the planet
    planet = input("Enter a planet: ")

    # Step 3: Check if the planet is in the dictionary and calculate the equivalent weight
    if planet in planet_gravity:
        gravity_percent = planet_gravity[planet]
        planet_weight = earth_weight * (gravity_percent / 100)
        
        # Step 4: Print the equivalent weight on the selected planet, rounded to 2 decimal places
        print(f"The equivalent weight on {planet}: {planet_weight:.2f}")
    else:
        print("Invalid planet name! Please enter a valid planet.")

if __name__ == "__main__":
    main()
