import random
import time
import sys

# ANSI escape codes for colors and formatting
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.05, color=RESET):
   # Prints text with delay to create a typing animation effect

    for char in color + text + RESET:   # Apply color before printing
        sys.stdout.write(char)          # Print without newline
        sys.stdout.flush()              # Force output immediately
        time.sleep(delay)               # Waiting before printing next char
    print()                             # Printing newline at the end

def roll_dice():
    # Welcome message
    slow_print("🎲 Welcome to the Python Dice Roller! 🎲\n", 0.03, CYAN)

    while True:
        # Get number of dice
        while True:
            try:
                slow_print("Enter number of dice to roll (1-9): ", 0.01, YELLOW)
                num_dice = int(input())  # Convert input to integer
                if 1 <= num_dice <= 9:   # Validate range
                    break
                else:
                    slow_print("Please enter a number between 1 and 9.", 0.02, RED)
            except ValueError:
                slow_print("Invalid input. Please enter an integer.", 0.02, RED)

        # Get number of sides per die
        while True:
            try:
                slow_print("Enter number of sides per die (2-32): ", 0.01, YELLOW)
                sides = int(input())
                if 2 <= sides <= 32:
                    break
                else:
                    slow_print("Please enter a number between 2 and 32.", 0.02, RED)
            except ValueError:
                slow_print("Invalid input. Please enter an integer.", 0.02, RED)

        # Get modifier
        while True:
            try:
                slow_print("Enter a modifier (0-99, can be negative): ", 0.01, YELLOW)
                modifier = int(input())
                if -99 <= modifier <= 99:
                    break
                else:
                    slow_print("Please enter a number between -99 and 99.", 0.02, RED)
            except ValueError:
                slow_print("Invalid input. Please enter an integer.", 0.02, RED)

        #  Rolling animation
        slow_print("\nRolling", 0.15, CYAN)
        for _ in range(3):              # Print 3 dots with delay
            slow_print(".", 0.2, CYAN)
            time.sleep(0.2)

        # Roll dice
        rolls = []         # List to store each die result
        print()
        for i in range(1, num_dice + 1):
            roll = random.randint(1, sides)  # Generate random number
            rolls.append(roll)               # Saving
            slow_print(f"Die {i}: {roll}", 0.05, YELLOW)
            time.sleep(0.2)

        # Calculate total
        total = sum(rolls) + modifier

        # Display results
        print(BLUE + "\n--------------------------" + RESET)
        slow_print(f"Rolls: {rolls}", 0.03, CYAN)
        slow_print(f"Modifier: {modifier:+}", 0.03, CYAN)
        slow_print(f"TOTAL: {total} !", 0.05, BOLD + GREEN)
        print(BLUE + "--------------------------\n" + RESET)

        # Ask to play again
        slow_print("Roll again? (y/n): ", 0.02, YELLOW)
        again = input().strip().lower()   # Remove spaces and lowercase
        if again != 'y':                  # If not 'y', exit the loop
            slow_print("\nThanks for playing! Goodbye! ", 0.04, MAGENTA)
            break

# Run the dice roller
roll_dice()
