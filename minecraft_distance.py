"""Minecraft Distance Calculator.

Calculates the straight-line distance between two coordinates in the game.
"""

import math


def calculate_distance(x1: float, z1: float, x2: float, z2: float) -> float:
    """Calculates Euclidean distance on the XZ plane."""
    return math.sqrt((x2 - x1) ** 2 + (z2 - z1) ** 2)


def main():
    print("====================================")
    print("    MINECRAFT DISTANCE CALCULATOR   ")
    print("====================================\n")

    try:
        print("--- Starting Point (Home/Base) ---")
        x1 = float(input("Enter X1: "))
        z1 = float(input("Enter Z1: "))

        print("\n--- Destination Point ---")
        x2 = float(input("Enter X2: "))
        z2 = float(input("Enter Z2: "))

        distance = calculate_distance(x1, z1, x2, z2)

        print(f"\n[RESULT] The distance is {round(distance, 2)} blocks!")

    except ValueError:
        print("\nError: Please enter valid numbers for coordinates!")


if __name__ == "__main__":
    main()