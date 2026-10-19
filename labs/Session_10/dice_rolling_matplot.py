"""Simulate rolling a fair die n times and show the empirical distribution.

Usage: python dice_rolling_matplot.py <number_of_simulations>
"""
import sys

import numpy as np
import matplotlib.pyplot as plt


def roll_dice():
    """This function simulates the rolling and returns the outcome"""
    rnumber = np.random.random()
    if rnumber <= 1/6:
        return 1
    elif rnumber <= 2/6:
        return 2
    elif rnumber <= 3/6:
        return 3
    elif rnumber <= 4/6:
        return 4
    elif rnumber <= 5/6:
        return 5
    else:
        return 6


def check_for_number(myinput):
    """Return the input as a positive integer, or stop the program with a message."""
    try:
        valid_input = int(myinput)
    except ValueError:
        print("The values are only integer numbers")
        sys.exit(1)
    if valid_input <= 0:
        print("The number of simulations must be positive")
        sys.exit(1)
    return valid_input


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python dice_rolling_matplot.py <number_of_simulations>")
        sys.exit(1)
    n_simulations = check_for_number(sys.argv[1])

    dice_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    counter = 1
    while counter <= n_simulations:
        out_roll = roll_dice()
        dice_dict[out_roll] += 1
        counter += 1

    print("Empirical distribution")
    for face, count in dice_dict.items():
        print(f"{face}: {count} ({count / n_simulations:.3f})")

    fig, ax = plt.subplots()
    ax.bar(list(dice_dict.keys()), list(dice_dict.values()))
    ax.set_xlabel("Face")
    ax.set_ylabel("Counts")
    ax.set_title("Empirical Distribution")
    plt.show()
