# movie_list.py

movies = ["The Matrix", "Inception", "Arrival", "Parasite"]
print(f"The list {movies} includes my top {len(movies)} favorite movies")
print(movies)

# 4a. sorted() vs original — sorted() returns a NEW list
print(sorted(movies))
print(movies)          # unchanged!

# 4b. .sort() — modifies in place
movies.sort()
print(movies)          # now sorted permanently

# 5. .append() to add a movie
movies.append("Spirited Away")
print(f"The list {movies} includes my top {len(movies)} favorite movies")