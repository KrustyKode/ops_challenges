# Create a list of ten string elements
fruits = ["apple", "banana", "cherry", "orange", "grapefruit", "kiwi", "mango", "pineapple", "strawberry", "watermelon"]

# Print the fourth element of the list
print(fruits[3])  

# Print the sixth through tenth element of the list
print(fruits[5:])
# Change the value of the seventh element to "onion"
fruits[6] = "onion"

# Use append() to add "grape" to the end of the list
fruits.append("grape")

# Use clear() to remove all elements from the list
fruits.clear()

# Use copy() to create a copy of the list
fruits_copy = fruits.copy()

# Use count() to count the number of times "apple" appears in the list
apple_count = fruits.count("apple")

# Use extend() to add the elements of the list ["apple", "banana"] to the end of the list
fruits.extend(["apple", "banana"])

# Use index() to find the index of the first occurrence of "banana" in the list
banana_index = fruits.index("banana")

# Use insert() to insert the element "cherry" at the beginning of the list
fruits.insert(0, "cherry")

# Use pop() to remove and return the last element of the list
last_fruit = fruits.pop()

# Use remove() to remove the first occurrence of "apple" from the list
fruits.remove("apple")

# Use reverse() to reverse the order of the elements in the list
fruits.reverse()

# Use sort() to sort the elements in the list in ascending order
fruits.sort()

# Create a tuple
fruits_tuple = ("apple", "banana", "cherry")

# Create a set
fruits_set = {"apple", "banana", "cherry"}

# Create a dictionary
fruits_dict = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
}

# Print the results
print(fruits)
print(fruits_copy)
print(apple_count)
print(banana_index)
print(last_fruit)
print(fruits_tuple)
print(fruits_set)
print(fruits_dict)
