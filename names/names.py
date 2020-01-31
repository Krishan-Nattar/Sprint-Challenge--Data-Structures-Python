import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

# O(n)
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# O(n)
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

binary_tree = BinarySearchTree(names_1[0])

for name_1 in names_1: # O(n)
    binary_tree.insert(name_1)

for name_2 in names_2: # O(n)
    if binary_tree.contains(name_2): # O(log n)
        duplicates.append(name_2)

# Runtime: 0.06696081161499023 seconds
# Runtime complexity: O(2n log n)
# n = input size of names. (They are different inputs, but i simplified it to one 'n' variable instead of n1 + n2, because they are both at 10,000 names)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
