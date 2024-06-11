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
from collections import (
    ChainMap,
    Counter,
    OrderedDict,
    UserDict,
    UserList,
    UserString,
    defaultdict,
    deque,
    namedtuple,
)


class BuiltInDataStructures:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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


class CollectionsModuleDemo:
    @staticmethod
    def counter_operations():
        """
        Demonstrates common operations with Counter from the collections module.
        """
        print("\n-------------Performing Counter Operations-------------\n")

        # Example: Counting words in a text
        text = "this is a test text with several words this is more text with some words"
        word_list = text.split()
        word_counter = Counter(word_list)
        print(f"Word counts: {word_counter}")

        # Finding the 3 most common words
        common_words = word_counter.most_common(3)
        print(f"3 most common words: {common_words}")

        # Example: Counting elements in a list of transactions
        transactions = ["buy", "sell", "buy", "sell", "buy", "hold"]
        transaction_counter = Counter(transactions)
        print(f"Transaction counts: {transaction_counter}")

        # Combining counters
        more_transactions = ["buy", "buy", "sell"]
        more_counter = Counter(more_transactions)
        combined_counter = transaction_counter + more_counter
        print(f"Combined transaction counts: {combined_counter}")

    @staticmethod
    def ordered_dict_operations():
        """
        Demonstrates common operations with OrderedDict from the collections module.
        """
        print("\n-------------Performing OrderedDict Operations-------------\n")

        # Example: Maintaining insertion order for processing tasks
        tasks = OrderedDict()
        tasks["task1"] = "clean house"
        tasks["task2"] = "write code"
        tasks["task3"] = "read book"
        tasks["task4"] = "exercise"

        print("Tasks in insertion order:")
        for task, description in tasks.items():
            print(f"{task}: {description}")

        # Move 'task3' to the end and 'task2' to the beginning
        tasks.move_to_end("task3")
        tasks.move_to_end("task2", last=False)
        print("\nTasks after reordering:")
        for task, description in tasks.items():
            print(f"{task}: {description}")

    @staticmethod
    def default_dict_operations():
        """
        Demonstrates common operations with defaultdict from the collections module.
        """
        print("\n-------------Performing defaultdict Operations-------------\n")

        # Example: Grouping a list of words by their first letter
        words = ["apple", "banana", "cherry", "avocado", "blueberry", "carrot"]
        grouped_words = defaultdict(list)
        for word in words:
            grouped_words[word[0]].append(word)

        print("Words grouped by their first letter:")
        for letter, word_list in grouped_words.items():
            print(f"{letter}: {word_list}")

        # Example: Counting occurrences of elements in a list
        elements = ["hydrogen", "helium", "hydrogen", "oxygen", "helium", "oxygen", "oxygen"]
        element_counter = defaultdict(int)
        for element in elements:
            element_counter[element] += 1

        print("Element counts:")
        for element, count in element_counter.items():
            print(f"{element}: {count}")

    @staticmethod
    def chain_map_operations():
        """
        Demonstrates common operations with ChainMap from the collections module.
        """
        print("\n-------------Performing ChainMap Operations-------------\n")

        # Example: Combining multiple dictionaries for configuration
        default_config = {"theme": "light", "show_sidebar": True, "font_size": "medium"}
        user_config = {"theme": "dark", "show_sidebar": False}
        runtime_config = {"show_sidebar": True, "font_size": "large"}

        combined_config = ChainMap(runtime_config, user_config, default_config)

        print("Combined configuration (runtime > user > default):")
        for key, value in combined_config.items():
            print(f"{key}: {value}")

        # Accessing values from the combined configuration
        print("\nAccessing specific values from the combined configuration:")
        print(f"Theme: {combined_config['theme']}")  # Should print 'dark' from user_config
        print(f"Show sidebar: {combined_config['show_sidebar']}")  # Should print 'True' from runtime_config
        print(f"Font size: {combined_config['font_size']}")  # Should print 'large' from runtime_config

        # Example: Updating configuration dynamically
        print("\nUpdating configuration dynamically:")
        runtime_config["theme"] = "blue"
        print(f"Updated theme: {combined_config['theme']}")  # Should print 'blue' from runtime_config

        # Example: Using ChainMap to manage scopes in a programming environment
        local_scope = {"variable": "local"}
        global_scope = {"variable": "global", "function": "global_func"}
        builtins_scope = {"function": "builtin_func", "object": "builtin_object"}

        scopes = ChainMap(local_scope, global_scope, builtins_scope)
        print("\nVariable lookup in multiple scopes:")
        print(f"Variable: {scopes['variable']}")  # Should print 'local'
        print(f"Function: {scopes['function']}")  # Should print 'global_func'
        print(f"Object: {scopes['object']}")  # Should print 'builtin_object'

    @staticmethod
    def named_tuple_operations():
        """
        Demonstrates common operations with namedtuple from the collections module.
        """
        print("\n-------------Performing namedtuple Operations-------------\n")

        # Example: Representing a point in 2D space
        Point = namedtuple("Point", ["x", "y"])
        point = Point(x=10, y=20)
        print(f"Point: {point}")

        # Example: Representing a person
        Person = namedtuple("Person", ["name", "age", "job"])
        person = Person(name="Alice", age=30, job="Engineer")
        print(f"Person: {person}")

        # Accessing attributes
        print(f"Name: {person.name}")
        print(f"Age: {person.age}")
        print(f"Job: {person.job}")

        # Converting to a dictionary
        person_dict = person._asdict()
        print(f"Person as dictionary: {person_dict}")

    @staticmethod
    def deque_operations():
        """
        Demonstrates common operations with deque from the collections module.
        """
        print("\n-------------Performing deque Operations-------------\n")

        # Example: Managing a queue of tasks
        task_queue = deque(["task1", "task2", "task3"])
        print(f"Initial queue: {task_queue}")

        # Adding tasks
        task_queue.append("task4")
        task_queue.appendleft("task0")
        print(f"Queue after adding tasks: {task_queue}")

        # Removing tasks
        task_queue.pop()
        task_queue.popleft()
        print(f"Queue after removing tasks: {task_queue}")

        # Rotating tasks
        task_queue.rotate(1)
        print(f"Queue after rotating right by 1: {task_queue}")
        task_queue.rotate(-1)
        print(f"Queue after rotating left by 1: {task_queue}")

    @staticmethod
    def user_dict_operations():
        """
        Demonstrates common operations with UserDict from the collections module.
        """
        print("\n-------------Performing UserDict Operations-------------\n")

        # Example: Creating a dictionary with custom behavior
        class MyUserDict(UserDict):
            def __init__(self, data=None, **kwargs):
                super().__init__(data, **kwargs)
                self.history = []

            def __setitem__(self, key, value):
                self.history.append((key, value))
                super().__setitem__(key, value)

        my_user_dict = MyUserDict()
        my_user_dict["a"] = 1
        my_user_dict["b"] = 2

        # Accessing and modifying elements
        print(f"User Dictionary: {my_user_dict = }")
        print(f"History of Dictionary: {my_user_dict.history}")

    @staticmethod
    def user_list_operations():
        """
        Demonstrates common operations with UserList from the collections module.
        """
        print("\n-------------Performing UserList Operations-------------\n")

        # Example: Creating a list with custom behavior
        class MyUserList(UserList):
            def __init__(self, data=None):
                super().__init__(data)

            def append(self, item):
                self.data.append(item.upper())

        my_user_list = MyUserList([1, 2, "small_case"])
        print(f"Initial list: {my_user_list}")

        # Modifying elements
        my_user_list.append("upper_case")
        print(f"Modified list: {my_user_list}")

    @staticmethod
    def user_string_operations():
        """
        Demonstrates common operations with UserString from the collections module.
        """
        print("\n-------------Performing UserString Operations-------------\n")

        # Example: Creating a string with custom behavior
        class MyUserString(UserString):
            def __init__(self, seq):
                print(f"Creating MyUserString with sequence: {seq}")
                super().__init__(seq)

            def is_palindrome(self):
                return self.data == self.data[::-1]

            def __getitem__(self, index):
                if isinstance(index, slice):
                    return MyUserString(self.data[index])
                return self.data[index]

        # Creating an instance of MyUserString
        my_user_string = MyUserString("madam")
        print(f"Initial user string: {my_user_string}")

        # Checking if the string is a palindrome
        print(f"Is palindrome: {my_user_string.is_palindrome()}")

        # Modifying strings (immutable, create a new instance)
        new_user_string = my_user_string + " is walking"
        print(f"After concatenation: {new_user_string}")

        # Upper and lower case
        print(f"Upper case: {my_user_string.upper()}")
        print(f"Lower case: {my_user_string.lower()}")

        # Slicing
        print(f"Sliced string (0:3): {my_user_string[0:3]}")

        # Checking palindrome on the sliced string
        print(f"Is sliced string a palindrome: {my_user_string[0:3].is_palindrome()}")


if __name__ == "__main__":
    # Built In Data Structures
    builtin_data_structure = BuiltInDataStructures()
    builtin_data_structure.list_operations()
    builtin_data_structure.dict_operations()
    builtin_data_structure.tuple_operations()
    builtin_data_structure.set_operations()
    builtin_data_structure.frozen_set_operations()
    builtin_data_structure.string_operations()
    builtin_data_structure.bytearray_operations()

    # Collections Module
    CollectionsModuleDemo.counter_operations()
    CollectionsModuleDemo.ordered_dict_operations()
    CollectionsModuleDemo.default_dict_operations()
    CollectionsModuleDemo.chain_map_operations()
    CollectionsModuleDemo.named_tuple_operations()
    CollectionsModuleDemo.deque_operations()
    CollectionsModuleDemo.user_dict_operations()
    CollectionsModuleDemo.user_list_operations()
    CollectionsModuleDemo.user_string_operations()
