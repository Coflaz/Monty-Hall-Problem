# **Monty Hall Problem Simulation**

This project simulates the famous **Monty Hall Problem** using Python, demonstrating that switching doors is statistically the best strategy for winning. It runs 100,000 simulations for different door scenarios (3, 10, and 10,000 doors) to analyze the winning probabilities when the contestant either stays with their initial choice or switches.

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results Visualization](#results-visualization)
- [Project Structure](#project-structure)
- [License](#license)

## **Introduction**
The Monty Hall problem is a probability puzzle based on a game show scenario. In this simulation, we test the strategy of "staying" vs. "switching" choices to statistically verify which yields a better chance of winning. The results are plotted to show that switching is the optimal choice.

## **Features**
- Simulates the Monty Hall problem for scenarios with 3, 10, and 10,000 doors.
- Performs 100,000 iterations per scenario to ensure statistically significant results.
- Compares win percentages for both "staying" and "switching" strategies.
- Visualizes results using `matplotlib` to highlight the advantage of switching.

## **Installation**
1. Ensure you have Python 3.x installed on your machine.
2. Install the required libraries using:
   ```bash
   pip install numpy pandas matplotlib
   ```

## **Usage**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/monty-hall-simulation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd monty-hall-simulation
   ```
3. Run the simulation script:
   ```bash
   python monty_hall_problem.py
   ```

## **Results Visualization**
The simulation results are displayed as a plot comparing the winning percentages for both strategies across different door configurations. The x-axis uses a logarithmic scale to better visualize the results for the varying number of doors.

## **Project Structure**
- `monty_hall_problem.py`: The main script containing the Monty Hall simulation logic and visualization code.
- `README.md`: Project documentation.

## **License**
This project is licensed under the MIT License.



