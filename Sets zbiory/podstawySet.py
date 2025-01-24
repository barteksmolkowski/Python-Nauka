tablica = [1, 2, 3, 3, 4, 3, 1, 3]
print(f"tab1: {tablica}")

# set()
liczby = set(tablica)
print(f"\ntab1: set(tab1): {liczby}")

# add
print("\ntab1.add(5)")
liczby.add(5)
print(f"tab1: {liczby}")

# remove()
print("\ntab1.remove(4)")
liczby.remove(4)
print(f"tab1: {liczby}")

# pop()
print("\ntab1.pop()")
liczby.pop()
print(f"tab1: {liczby}")

# clear()
print("\ntab1.clear()")
liczby.clear()
print(f"tab1: {liczby}")

# copy()
print("\ntab2 = tab1.copy()")
wszystkieliczby = liczby.copy()
print(f"tab2: {wszystkieliczby}")

# union()
print("\ntab2 = {1, 2, 3}.union({3, 4, 5})")
combined_set = {1, 2, 3}.union({3, 4, 5})
print(f"tab2: {combined_set}")

# intersection()
print("\ntab2 = {1, 2, 3}.intersection({3, 4, 5})")
common_set = {1, 2, 3}.intersection({3, 4, 5})
print(f"Intersection: {common_set}")

# difference()
print("\ntab2 = {1, 2, 3}.difference({3, 4, 5})")
difference_set = {1, 2, 3}.difference({3, 4, 5})
print(f"Difference: {difference_set}")

