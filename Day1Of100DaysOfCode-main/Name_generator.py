import random

def generate_band_name():
    print("Let's generate a name for your rockin' band!")

    while True:  # Loop until valid birth city is entered
        birth_city = input("What's your birth city?: ")
        if birth_city:  # Check for empty input
            break
        print("Please enter a valid city name.")

    while True:  # Loop until valid pet name is entered
        pet_name = input("What was your first pet's name?: ")
        if pet_name:  # Check for empty input
            break
        print("Please enter a valid pet name.")

    try:
        num_siblings = int(input("How many siblings do you have (enter a number): "))
    except ValueError:
        print("Please enter a valid number of siblings.")
        return  # Exit function if invalid input

    adjectives = ["Sonic", "Cosmic", "Electric", "Rebel", "Groovy"]
    adjective = random.choice(adjectives)

    # Creative combination options (choose one):
    # option 1: first 3 letters of city, last 2 letters of pet name, add sibling count
    # band_name = adjective + " " + birth_city[:3] + pet_name[-2:] + f"'s ({num_siblings})"
    # option 2: first letter of city, all of pet name, sibling count as Roman numeral
    roman_numerals = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
    sibling_roman = roman_numerals.get(num_siblings, "")  # Handle non-existent Roman numeral
    band_name = adjective + " " + birth_city[0] + pet_name + sibling_roman

    print(f"Your band could be called: {band_name}!")

generate_band_name()
