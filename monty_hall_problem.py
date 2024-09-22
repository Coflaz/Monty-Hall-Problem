# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to simulate the Monty Hall problem
def simulate_monty_hall(num_doors, num_simulations):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_simulations):
        # Randomly place the car behind one of the doors
        car_position = np.random.randint(0, num_doors)
        
        # Contestant makes their initial choice
        initial_choice = np.random.randint(0, num_doors)

        # Host reveals a goat door, i.e., not the door chosen by contestant and not the car door
        # Number of doors that can be opened by the host
        num_doors_to_open = num_doors - 2
        available_doors = [door for door in range(num_doors) if door != initial_choice and door != car_position]
        doors_opened_by_host = np.random.choice(available_doors, size=num_doors_to_open, replace=False)
        
        # If the contestant stays
        if initial_choice == car_position:
            stay_wins += 1
        else:
            switch_wins += 1

    return stay_wins, switch_wins

# Define parameters
num_simulations = 100000
door_configs = [3, 10, 10000]  # Different scenarios for the Monty Hall problem

# Store results
results = []
for num_doors in door_configs:
    stay_wins, switch_wins = simulate_monty_hall(num_doors, num_simulations)
    results.append({
        'num_doors': num_doors,
        'stay_wins': stay_wins,
        'switch_wins': switch_wins,
        'stay_win_percentage': (stay_wins / num_simulations) * 100,
        'switch_win_percentage': (switch_wins / num_simulations) * 100
    })

# Create a DataFrame to store results
df_results = pd.DataFrame(results)

# Display the simulation results
print(df_results)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(df_results['num_doors'], df_results['stay_win_percentage'], label='Stay Win %', marker='o')
plt.plot(df_results['num_doors'], df_results['switch_win_percentage'], label='Switch Win %', marker='o')

# Customize the plot
plt.title('Monty Hall Problem: Stay vs Switch Win Percentage')
plt.xlabel('Number of Doors')
plt.ylabel('Winning Percentage (%)')
plt.xscale('log')
plt.legend()
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Show the plot
plt.show()
