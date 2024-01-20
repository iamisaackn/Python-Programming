# ----------------------------------------------- EASY ------------------------------------------------------------

# ------------ 1. Coin Toss ----------------------------
'''
You flip a fair coin. What is the probability of getting heads?
'''

# Import random module for random number generation
import random

def coin_toss():
    # Simulate a coin toss (0 for heads, 1 for tails)
    outcome = random.choice([0, 1])

    # Check the outcome and return the result
    if outcome == 0:
        return "Heads"
    else:
        return "Tails"

# Perform multiple coin tosses to approximate the probability of getting heads
num_tosses = 10000  # You can adjust this number based on your preference

# Count the number of heads
heads_count = sum(1 for _ in range(num_tosses) if coin_toss() == "Heads")

# Calculate the probability of getting heads
probability_heads = heads_count / num_tosses

# Print the result
print(f"Probability of getting heads: {probability_heads}")


# -------------------------- 2. Dice Roll ------------------------------------------------
'''
You roll a six-sided die. What is the probability of rolling x?
'''

import random

def dice_roll():
    roll = random.randint(1, 6)
    return roll

num_rolls = 100000

x = int(input("Enter a number between 1 and 6: "))

try: 
    if x in range(1, 7):
        x_count = sum(1 for _ in range(num_rolls) if dice_roll()== x)
        probability = x_count / num_rolls
        print(f"Probability of rolling {x}: {probability}")

    else: 
        print("Please enter a number between 1 and 6.")

except ValueError:
    print("Invalid input. Please enter a valid number between 1 and 6.")


# -------------------------- 3. Card Draw ---------------------------------
'''
You draw a card from a standard deck of 52 cards. What is the probability of drawing a heart?
'''
num_hearts = 13
total_cards = 52

probability_heads = num_hearts/total_cards

print(f"The probabilyty of getting a head: {probability_heads}")

# Example 2