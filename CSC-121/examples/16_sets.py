#  Program: 16_sets.py
#  Author: Michael Souther
#  Date: 09/13/2020
# Create an empty set
example = set()
# Add elements to the set
example.add(42)
example.add(True)
example.add(3.14)
example.add('Hello')
# Print the set 
print(example)
# Remove an element from the set
example.remove(True)
print(example)
# Try to remove a element that does not exist
# Uncomment the code below see what happens
# example.remove(53)
# Using discard to remove an element safely
example.discard(53)
print(example)

# sets of integers 1 - 10
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
prime = {2, 3, 5, 7}
# Union 
print(even.union(odd))
print(odd.union(even))
# Intersection
print(even.intersection(odd))
print(odd.intersection(prime))