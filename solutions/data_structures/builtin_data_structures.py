"""
This file contains notes about built-in data structures in Python. Reference:
https://www.geeksforgeeks.org/python-data-structures/

You can find detailed notes in (docs/BuiltIn_Data_Structures.md) and code explanations below.
Here’s a high-level overview of what we’ll cover:

└── Python Built-in Data Structures
    └── Lists
    └── Dictionaries
    └── Tuples
    └── Sets
    └── Frozen Sets
    └── Strings
    └── Bytearrays
└── Collections Module
    └── Counter
    └── OrderedDict
    └── DefaultDict
    └── ChainMap
    └── NamedTuple
    └── Deque
    └── UserDict
    └── UserList
    └── UserString
"""


def list_operations():
    """
    Demonstrates common list operations in Python.
    """
    print("\n-------------Performing List Operations-------------\n")

    # List Creation
    my_list = [1, 2, 3, 4, 5]

    # Accessing Elements
    print(f"{my_list = }")
    print(f"First element: {my_list[0]}")
    print(f"Last element: {my_list[-1]}")
    print(f"Elements from index 1 to 3: {my_list[1:3]}")

    # Modifying Elements
    my_list[0] = 10
    print(f"After modifying the first element: {my_list}")

    # Adding Elements
    my_list.append(6)
    print(f"After appending 6: {my_list}")

    my_list.insert(1, 7)
    print(f"After inserting 7 at index 1: {my_list}")

    # Removing Elements
    my_list.remove(7)
    print(f"After removing 7: {my_list}")

    del my_list[2]
    print(f"After deleting element at index 2: {my_list}")

    # Concatenation
    new_list = my_list + [7, 8]
    print(f"New list by concatenating my_list with [7, 8]: {new_list}")

    # Repetition
    repeated_list = my_list * 2
    print(f"New list by repeating my_list twice: {repeated_list}")

    # Length
    print(f"Length of my_list: {len(my_list)}")

    # Reversing
    my_list.reverse()
    print(f"Reversed my_list: {my_list}")

    # Sorting
    my_list.sort()
    print(f"Sorted in ascending order: {my_list}")

    my_list.sort(reverse=True)
    print(f"Sorted in descending order: {my_list}")

    # Searching
    print(f"Is 2 in my_list?: {2 in my_list}")
    print(f"Is 100 in my_list?: {100 in my_list}")

    # Indexing and Slicing
    print(f"Index of the first occurrence of 6: {my_list.index(6)}")

    # Other Operations
    print(f"Minimum value: {min(my_list)}")
    print(f"Maximum value: {max(my_list)}")
    print(f"Sum of values: {sum(my_list)}")


def dict_operations():
    """
    Demonstrates common dictionary operations in Python.
    """
    print("\n-------------Performing Dictionary Operations-------------\n")

    # Dictionary Creation
    my_dict = {"name": "John Doe", "age": 30, "city": "New York"}
    empty_dict = {}

    # Accessing Values
    print(f"{my_dict = }")
    print(f"Name: {my_dict['name']}")
    print(f"Age: {my_dict.get('age', 'N/A')}")

    # Modifying Values
    my_dict["age"] = 31
    print(f"After modifying age: {my_dict}")

    # Adding Key-Value Pairs
    my_dict["occupation"] = "Software Engineer"
    print(f"After adding occupation: {my_dict}")

    # Removing Key-Value Pairs
    del my_dict["city"]
    print(f"After removing city: {my_dict}")

    # Checking Key Existence
    print(f"Does 'name' key exist?: {'name' in my_dict}")
    print(f"Does 'country' key exist?: {'country' in my_dict}")

    # Iterating over Keys and Values
    print("\nIterating over keys:")
    for key in my_dict:
        print(key)

    print("\nIterating over key-value pairs:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

    # Getting Keys, Values, and Key-Value Pairs
    print(f"Keys: {my_dict.keys()}")
    print(f"Values: {my_dict.values()}")
    print(f"Items: {my_dict.items()}")

    # Copying a Dictionary
    new_dict = my_dict.copy()
    print(f"New dictionary: {new_dict}")

    # Updating a Dictionary
    new_dict.update({"city": "San Francisco"})
    print(f"Updated dictionary: {new_dict}")

    # Clearing a Dictionary
    new_dict.clear()
    print(f"Cleared dictionary: {new_dict}")

    # Nested Dictionaries
    nested_dict = {"person1": {"name": "Alice", "age": 25}, "person2": {"name": "Bob", "age": 30}}
    print(f"Nested dictionary: {nested_dict}")
    print(f"Alice's age: {nested_dict['person1']['age']}")

    # Dictionary Comprehension
    squares = {x: x**2 for x in range(1, 6)}
    print(f"Dictionary comprehension: {squares}")

    # Length
    print(f"Length of my_dict: {len(my_dict)}")

    # Checking if empty
    print(f"Is my_dict empty?: {not my_dict}")
    print(f"Is empty_dict empty?: {not empty_dict}")


def tuple_operations():
    """
    Demonstrates common tuple operations in Python.
    """
    print("\n-------------Performing Tuple Operations-------------\n")

    # Tuple Creation
    my_tuple = ("John Doe", 30, "New York")
    empty_tuple = ()

    # Accessing Elements
    print(f"{my_tuple = }")
    print(f"Name: {my_tuple[0]}")
    print(f"Age: {my_tuple[1]}")

    # Tuples are immutable, so elements cannot be modified directly
    # Concatenating Tuples
    additional_info = ("Software Engineer",)
    combined_tuple = my_tuple + additional_info
    print(f"Combined tuple: {combined_tuple}")

    # Slicing a Tuple
    sliced_tuple = combined_tuple[1:3]
    print(f"Sliced tuple: {sliced_tuple}")

    # Checking Element Existence
    print(f"Is 'John Doe' in the tuple?: {'John Doe' in combined_tuple}")
    print(f"Is 'Los Angeles' in the tuple?: {'Los Angeles' in combined_tuple}")

    # Iterating over a Tuple
    print("\nIterating over the tuple:")
    for item in combined_tuple:
        print(item)

    # Tuple Unpacking
    name, age, city, occupation = combined_tuple
    print(f"\nUnpacked values: {name}, {age}, {city}, {occupation}")

    # Length of a Tuple
    print(f"Length of my_tuple: {len(my_tuple)}")

    # Checking if a Tuple is Empty
    print(f"Is my_tuple empty?: {not my_tuple}")
    print(f"Is empty_tuple empty?: {not empty_tuple}")

    # Tuple Repetition
    repeated_tuple = my_tuple * 2
    print(f"Repeated tuple: {repeated_tuple}")

    # Finding the Index of an Element
    index_of_age = my_tuple.index(30)
    print(f"Index of age (30): {index_of_age}")

    # Counting Occurrences of an Element
    count_of_new_york = my_tuple.count("New York")
    print(f"Count of 'New York': {count_of_new_york}")


def set_operations():
    """
    Demonstrates common set operations in Python.
    """
    print("\n-------------Performing Set Operations-------------\n")

    # Set Creation
    my_set = {"apple", "banana", "cherry"}
    empty_set = set()

    # Adding Elements
    print(f"{my_set = }")
    my_set.add("orange")
    print(f"After adding 'orange': {my_set}")

    # Removing Elements
    my_set.remove("banana")
    print(f"After removing 'banana': {my_set}")

    my_set.discard("grape")
    print(f"After discarding 'grape': {my_set}")

    # Membership Testing
    print(f"'apple' in my_set: {'apple' in my_set}")
    print(f"'grape' in my_set: {'grape' in my_set}")

    # Set Operations
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    # Union
    union_set = set1 | set2
    print(f"Union of {set1} and {set2}: {union_set}")

    # Intersection
    intersection_set = set1 & set2
    print(f"Intersection of {set1} and {set2}: {intersection_set}")

    # Difference
    difference_set = set1 - set2
    print(f"Difference of {set1} and {set2}: {difference_set}")

    # Symmetric Difference
    symmetric_difference_set = set1 ^ set2
    print(f"Symmetric difference of {set1} and {set2}: {symmetric_difference_set}")

    # Set Comprehension
    set_comprehension = {x for x in range(10) if x % 2 == 0}
    print(f"Set comprehension: {set_comprehension}")

    # Length
    print(f"Length of my_set: {len(my_set)}")

    # Checking if Empty
    print(f"Is my_set empty?: {not my_set}")
    print(f"Is empty_set empty?: {not empty_set}")

    # Iterating over a Set
    print("\nIterating over my_set:")
    for item in my_set:
        print(item)


def frozen_set_operations():
    """
    Demonstrates common frozen set operations in Python.
    """
    print("\n-------------Performing Frozen Set Operations-------------\n")

    # Frozen Set Creation
    my_frozen_set = frozenset(["apple", "banana", "cherry"])

    # Accessing Elements (not possible, frozen sets are immutable and do not support indexing)

    # Membership Testing
    print(f"'apple' in my_frozen_set: {'apple' in my_frozen_set}")
    print(f"'grape' in my_frozen_set: {'grape' in my_frozen_set}")

    # Frozen Set Operations (similar to set operations, but results in frozen sets)
    frozen_set1 = frozenset([1, 2, 3])
    frozen_set2 = frozenset([3, 4, 5])

    # Union
    frozen_union = frozen_set1 | frozen_set2
    print(f"Union of {frozen_set1} and {frozen_set2}: {frozen_union}")

    # Intersection
    frozen_intersection = frozen_set1 & frozen_set2
    print(f"Intersection of {frozen_set1} and {frozen_set2}: {frozen_intersection}")

    # Difference
    frozen_difference = frozen_set1 - frozen_set2
    print(f"Difference of {frozen_set1} and {frozen_set2}: {frozen_difference}")

    # Symmetric Difference
    frozen_symmetric_difference = frozen_set1 ^ frozen_set2
    print(f"Symmetric difference of {frozen_set1} and {frozen_set2}: {frozen_symmetric_difference}")

    # Length
    print(f"Length of my_frozen_set: {len(my_frozen_set)}")

    # Checking if Empty (always returns False, frozen sets are never empty)
    print(f"Is my_frozen_set empty?: {not my_frozen_set}")

    # Iterating over a Frozen Set
    print("\nIterating over my_frozen_set:")
    for item in my_frozen_set:
        print(item)


def string_operations():
    """
    Demonstrates common string operations in Python.
    """
    print("\n-------------Performing String Operations-------------\n")

    # String Creation
    my_string = "Hello, World!"
    empty_string = ""

    # Accessing Characters
    print(f"{my_string = }")
    print(f"First character: {my_string[0]}")
    print(f"Last character: {my_string[-1]}")

    # Slicing a String
    print(f"Slicing from index 1 to 5: {my_string[1:5]}")

    # Modifying Strings (strings are immutable, so we create a new string)
    new_string = my_string.replace("World", "Python")
    print(f"New string: {new_string}")

    # Concatenating Strings
    concatenated_string = my_string + " How are you?"
    print(f"Concatenated string: {concatenated_string}")

    # Repetition
    repeated_string = my_string * 2
    print(f"Repeated string: {repeated_string}")

    # Length of a String
    print(f"Length of my_string: {len(my_string)}")

    # Checking if Empty
    print(f"Is my_string empty?: {not my_string}")
    print(f"Is empty_string empty?: {not empty_string}")

    # Checking Substring Existence
    print(f"Does 'Hello' exist in my_string?: {'Hello' in my_string}")
    print(f"Does 'Python' exist in my_string?: {'Python' in my_string}")

    # Iterating over a String
    print("\nIterating over my_string:")
    for char in my_string:
        print(char)

    # String Methods
    print(f"Uppercase: {my_string.upper()}")
    print(f"Lowercase: {my_string.lower()}")
    print(f"Title Case: {my_string.title()}")
    print(f"Split: {my_string.split(',')}")
    print(f"Joined: {' '.join(['Hello', 'Python'])}")
    print(f"Stripped: {'   Hello, Python!   '.strip()}")
    print(f"Center aligned: {'Hello'.center(20, '*')}")

    # Formatting Strings
    name, age = "Suresh", 20
    formatted_string = f"My name is {name} and I am {age} years old."
    print(f"Formatted string: {formatted_string}")

    # Finding and Counting
    print(f"Index of 'World': {my_string.find('World')}")
    print(f"Count of 'l': {my_string.count('l')}")


def bytearray_operations():
    """
    Demonstrates common bytearray operations in Python.
    """
    print("\n-------------Performing Bytearray Operations-------------\n")

    # Bytearray Creation
    my_bytearray = bytearray("Hello, World!", "utf-8")
    empty_bytearray = bytearray()

    # Accessing Elements
    print(f"{my_bytearray = }")
    print(f"First element: {my_bytearray[0]}")
    print(f"Last element: {my_bytearray[-1]}")

    # Modifying Elements
    my_bytearray[0] = 67
    print(f"After modifying the first element: {my_bytearray}")

    # Adding Elements
    my_bytearray.append(33)
    print(f"After appending 33: {my_bytearray}")

    # Removing Elements
    del my_bytearray[-1]
    print(f"After deleting the last element: {my_bytearray}")

    # Concatenation
    concatenated_bytearray = my_bytearray + bytearray(" How are you?", "utf-8")
    print(f"Concatenated bytearray: {concatenated_bytearray}")

    # Repetition
    repeated_bytearray = my_bytearray * 2
    print(f"Repeated bytearray: {repeated_bytearray}")

    # Length
    print(f"Length of my_bytearray: {len(my_bytearray)}")

    # Checking if Empty
    print(f"Is my_bytearray empty?: {not my_bytearray}")
    print(f"Is empty_bytearray empty?: {not empty_bytearray}")

    # Iterating over a Bytearray
    print("\nIterating over my_bytearray:")
    for byte in my_bytearray:
        print(byte)

    # Slicing a Bytearray
    sliced_bytearray = my_bytearray[1:5]
    print(f"Sliced bytearray: {sliced_bytearray}")

    # Finding and Counting
    print(f"Index of 'World': {my_bytearray.find(b'World')}")
    print(f"Count of 'o': {my_bytearray.count(b'o')}")

    # Converting to a String
    bytearray_to_string = my_bytearray.decode("utf-8")
    print(f"Bytearray to string: {bytearray_to_string}")

    # Converting from a String
    string_to_bytearray = bytearray("Python is fun!", "utf-8")
    print(f"String to bytearray: {string_to_bytearray}")


if __name__ == "__main__":
    list_operations()
    dict_operations()
    tuple_operations()
    set_operations()
    frozen_set_operations()
    string_operations()
    bytearray_operations()
