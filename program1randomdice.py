import random

def randDice():
    # Roll two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # Sum the rolls
    return dice1 + dice2

# Mainline
def main():
    total_sum = 0
    num_rolls = 100

    for _ in range(num_rolls):
        total_sum += randDice()

    average_roll = total_sum / num_rolls
    # Print the average, rounded to the nearest 0.01
    print(f"Average of 100 rolls: {average_roll:.2f}")

if __name__ == "__main__":
    main()
