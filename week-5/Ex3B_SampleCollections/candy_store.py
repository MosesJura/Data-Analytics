# candy_store.py

# 2. Two tuples
candies = ("gummy bears", "sour worms", "jelly beans", "lollipops")
flavors = ("cherry", "watermelon", "green apple", "blue raspberry")

# 3. Set of combinations (tuples inside a set)
combos = set()
combos.add((candies[0], flavors[0]))   # gummy bears + cherry
combos.add((candies[1], flavors[1]))   # sour worms + watermelon
combos.add((candies[2], flavors[2]))   # jelly beans + green apple
combos.add((candies[3], flavors[3]))   # lollipops + blue raspberry

# 4. Output message
print("Today's candy options include:")
for combo in combos:
    print(f"  {combo[0]} ({combo[1]})")

# 5. Print multiple times — notice order changes
print("\nRun 1:")
print(combos)
print("\nRun 2:")
print(combos)
print("\nRun 3:")
print(combos)