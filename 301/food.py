def manipulate_fruits():
  """
  This function manipulates a list of fruits, performing various operations
  including slicing, modifications, data structure conversions, and printing.
  """
  # Print a slice of the fruits list (index 3 to 5).
  print(fruits[3:6])

  # Replace element at index 6 with "onion".
  fruits[6:7] = ["onion"]

  # Add "grape" to the end of the list using chainable assignment.
  fruits += ["grape"]

  # Create a copy of the fruits list using list comprehension.
  fruits_copy = [fruit for fruit in fruits]

  # Get the number of occurrences of "apple" using built-in methods.
  apple_count = fruits.count("apple")

  # Extend the list with additional elements using chainable assignment.
  fruits += ["apple", "banana"]

  # Find the index of the first "banana" using built-in methods.
  banana_index = fruits.index("banana")

  # Insert "cherry" at the beginning of the list using built-in methods.
  fruits.insert(0, "cherry")

  # Pop the last element from the list and store it in a variable.
  last_fruit = fruits.pop()

  # Remove the first occurrence of "apple" using built-in methods.
  fruits.remove("apple")

  # Print the fruits list in reverse order using loop and reversed function.
  for fruit in reversed(fruits):
      print(fruit)

  # Create a sorted copy of the fruits list using the built-in sorted function.
  sorted_fruits = sorted(fruits)

  # Create a tuple and set containing fruits using set literals.
  fruits_tuple = ("apple", "banana", "cherry")
  fruits_set = {"apple", "banana", "cherry"}

  # Create a dictionary associating fruits with their colors using literal syntax.
  fruits_dict = {"apple": "red", "banana": "yellow", "cherry": "red"}

  # Print all the manipulated data structures:
  print(fruits)
  print(fruits_copy)
  print(apple_count)
  print(banana_index)
  print(last_fruit)
  print(fruits_tuple)
  print(fruits_set)
  print(fruits_dict)
  print(sorted_fruits)

# Call the function
manipulate_fruits()
