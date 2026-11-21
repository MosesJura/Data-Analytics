# number_guesser.py
# Bonus project — guess a random number between 1 and 100
# WITHOUT using the random module.
# Uses: set (unique pool), list (shuffled pool), while (loop)

import time

# 1. Build a pool of possible numbers (1-100)
number_pool = list(range(1, 101))

# 2. "Shuffle" without the random module:
#    use the current time (microseconds) as a seed for a deterministic
#    index jump — this gives us pseudo-random ordering.
seed = int(time.time() * 1000000) % len(number_pool)
shuffled = number_pool[seed:] + number_pool[:seed]

# 3. Pick the first number — it's effectively "random"
secret_number = shuffled[0]

# --- Bonus trackers ---
guess_count = 0
guesses = []

print(f"I'm thinking of a number between 1 and 100.")
print("Can you guess it?")

# 4. Loop until correct
while True:
    raw = input("Your guess: ")

    # Bonus d) safe for non-numeric input
    try:
        guess = int(raw)
    except ValueError:
        print("Please enter a whole number (1–100).")
        continue

    guess_count += 1
    guesses.append(guess)

    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print(f"Correct! You got it in {guess_count} guesses.")
        break

# 5. Bonus outputs
print(f"Your guesses were: {guesses}")

if guess_count < 5:
    print("You're awesome — under 5 guesses!")

    