# **Monty Hall Problem Simulation**

This Python project offers a deep dive into the famous **Monty Hall Problem**, providing a statistical simulation that's ideal for **statisticians**, **mathematicians**, **behavioral economists**, or any **curious individuals** interested in understanding this classic probability puzzle. The code is designed to be adaptable, so feel free to **copy, test, modify**, and explore how this paradox can support your theories and implications in various domains.

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [The Brilliance of Marilyn vos Savant](#the-brilliance-of-marilyn-vos-savant)
- [Relation to Behavioral Economics](#relation-to-behavioral-economics)
- [Installation](#installation)
- [Usage](#usage)
- [Results Visualization](#results-visualization)
- [Project Structure](#project-structure)
- [License](#license)

## **Introduction**
The Monty Hall problem is a probability puzzle rooted in a game show scenario. This simulation uses Python to test the strategy of "staying" vs. "switching" choices, statistically verifying which yields a better chance of winning. By running simulations across multiple door scenarios (3, 10, and 10,000 doors), the project demonstrates the statistically optimal choice: **switching**.

## **Features**
- Simulates the Monty Hall problem for different scenarios (3, 10, and 10,000 doors).
- Conducts 100,000 iterations per scenario for robust statistical significance.
- Compares win percentages for both "staying" and "switching" strategies.
- Provides clear visualizations using `matplotlib` to highlight the advantage of switching.

## **The Brilliance of Marilyn vos Savant**
In 1990, **Marilyn vos Savant**, famed for having one of the world's highest recorded IQs, answered a reader’s query on the Monty Hall Problem in her “Ask Marilyn” column. She argued that **switching doors gives a 2/3 chance of winning**, compared to a 1/3 chance for staying with the initial choice (Crockett, 2015). This sparked a massive backlash, with over **10,000 letters**, many from academics and Ph.D. holders, arguing that her solution was incorrect (Crockett, 2015). 

One letter stated, *“There is enough mathematical illiteracy in this country, and we don’t need the world’s highest IQ propagating more”* (Crockett, 2015). However, vos Savant was ultimately proven right, demonstrating how even experts can overlook the subtleties of probability. Her explanation not only illuminated the correct solution but also challenged the assumptions of intellectual authority, leading to broader discussions in mathematics and economics.

**Citation:** 
Crockett, Z. (2015). The Time Everyone “Corrected” the World’s Smartest Woman. *Priceonomics*. Retrieved from [Priceonomics](https://priceonomics.com/the-time-everyone-corrected-the-worlds-smartest/)

## **Relation to Behavioral Economics**
The Monty Hall problem is more than just a mathematical curiosity; it serves as a crucial example in **behavioral economics**. The problem highlights how **cognitive biases**—such as the tendency to **stick with an initial decision (anchoring effect)** and the **misperception of probabilities**—can influence human behavior. Research has shown that most people fail to switch, even when it's the optimal choice, underscoring how individuals often struggle with probability-based decisions (Saenen et al., 2018).

Understanding the Monty Hall problem helps economists and psychologists gain insights into **decision-making processes**, risk assessment, and how individuals respond to uncertainty, making it a valuable tool in studying economic behavior.

**Citation:**
Saenen, L., Heyvaert, M., Van Dooren, W., Schaeken, W., & Onghena, P. (2018). Why Humans Fail in Solving the Monty Hall Dilemma: A Systematic Review. *Psychologica Belgica*, 58(1), 128–158. https://doi.org/10.5334/pb.274

## **Installation**
1. Ensure Python 3.x is installed.
2. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib
   ```

## **Usage**
1. Clone the repository:
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
The plot below illustrates the winning percentages for both "Stay" and "Switch" strategies across different numbers of doors. As shown, the "Switch" strategy consistently yields a higher winning percentage, confirming it as the optimal approach.

![Monty Hall Problem Results](https://github.com/user-attachments/assets/103c8d0e-f23d-4f4e-9bbc-314d94049b75)

## **Project Structure**
- `monty_hall_problem.py`: Main script containing the simulation and visualization logic.
- `README.md`: Documentation.

## **License**
This project is licensed under the MIT License.







