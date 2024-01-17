# Program that allows to calculate average radiation level based on user input for a specific location 
# Function to calculate average radiation
def average_radiation(levels):
    return sum(levels) / len(levels)

# List and dictionary to hold predefined variable
locations = ["Urban", "Forest"]
levels = {
    "Urban": [23, 33, 32, 27, 45, 17, 45, 33, 42, 28],
    "Forest": [14, 9, 22, 18, 28, 15, 4, 18, 22, 8]
}

for location in locations:
    print(f"Processing {location} with measurements {levels[location]}")
    average_rad = average_radiation(levels[location])
    print(f"{location} Average Radiation Level: {average_rad}")

# While loop to allow user to enter measurements until they want to exit
chosen_location = input("Please choose location (Urban or Forest): ").lower()
if chosen_location.capitalize() not in locations:
    print("Invalid location. Exiting.")
else:
    measurements = []
    while True:
        try:
            new_level = input(f"Enter radiation level for {chosen_location.capitalize()} (type 'exit' to stop): ")
            if new_level.lower() == 'exit':
                print("Exiting input loop")
                break
            else:
                measurements.append(int(new_level))
                print(f"Debug: Level added for {chosen_location.capitalize()}.")
        except ValueError:
            print("Please enter a valid level.")

    # Display average radiation if measurement is present
    if measurements:
        average_rad = average_radiation(measurements)
        print(f"Average Radiation Level for {chosen_location.capitalize()}: {average_rad}")
    else:
        print(f"Debug: No measurements entered for {chosen_location.capitalize()}.")