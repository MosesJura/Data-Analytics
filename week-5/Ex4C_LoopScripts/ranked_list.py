# ranked_list.py

favorites = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

# 3. Numbered list starting at 1
for i, item in enumerate(favorites, start=1):
    if i == 1:
        print(f"{i}. {item}  <-- top pick!")
    else:
        print(f"{i}. {item}")

# 5. BONUS: reverse order (still numbered 1–5)
print("\nReversed:")
reversed_list = list(reversed(favorites))
for i, item in enumerate(reversed_list, start=1):
    print(f"{i}. {item}")