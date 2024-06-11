# Python Data Structures and Algorithms

## Index
1. [Introduction](#introduction)
2. [Python Built-in Data Structures](#python-built-in-data-structures)
    - [Lists](#1-lists)
    - [Dictionaries](#2-dictionaries)
    - [Tuples](#3-tuples)
    - [Sets](#4-sets)
    - [Frozen Sets](#5-frozen-sets)
    - [Strings](#6-strings)
    - [Bytearrays](#7-bytearrays)
3. [Collections Module](#collections-module)
    - [Counter](#counter)
    - [OrderedDict](#ordereddict)
    - [DefaultDict](#defaultdict)
    - [ChainMap](#chainmap)
    - [NamedTuple](#namedtuple)
    - [Deque](#deque)
    - [UserDict](#userdict)
    - [UserList](#userlist)
    - [UserString](#userstring)

## Introduction

Data structures are the building blocks of efficient algorithms and form the backbone of any complex program. They provide **organized ways to store and manage data** in computer memory, allowing for **optimized access, retrieval, and manipulation**.  Choosing the right data structure can significantly impact a program's performance, especially when dealing with large datasets.  Different data structures have their own strengths and weaknesses, making them suitable for specific tasks.

For instance, arrays offer **fast access to elements by index**, while linked lists excel at **insertions and deletions**. Understanding these characteristics is crucial for any programmer aiming to write efficient and scalable code.

## Python Built-in Data Structures:

This section delves into Python's fundamental built-in data structures, exploring their mutability, time complexities for common operations, strengths, and weaknesses.

### 1. Lists:

**Definition:** An ordered, mutable collection of items. Lists are Python's version of dynamic arrays.

**Example:**
```python
my_list = [1, "hello", 3.14, True]
```

- **Mutability:** Mutable - Elements can be added, removed, or changed after creation.
- **Time Complexity:**
    - Accessing element: O(1)
    - Searching element: O(n)
    - Inserting/Deleting at beginning/middle: O(n)
    - Deleting at end: O(1)
    - Inserting at end:
      1. When preallocated memory is available: O(1)
      2. When preallocated memory is full: O(n)


- **Strengths:**
    - Versatile: Can store heterogeneous data types.
    - Ordered: Maintains insertion order.
    - Supports indexing and slicing for easy access and manipulation.
- **Weaknesses:**
    - Slow for insertion/deletion at the beginning or middle due to element shifting.
    - Searching can be inefficient for large lists.
---
**Why insertion at the end of a list can be O(n):**

Python lists are dynamically sized. When you append to a list that's full, Python creates a new list with a larger capacity (usually about double) and copies all the existing elements to this new list. This copying operation takes O(n) time. However, this resizing doesn't happen on every insertion, making the average time complexity of appending O(1) (amortized).

---
### 2. Dictionaries:

**Definition:** An unordered collection of key-value pairs, implemented using hash tables. Dictionaries are optimized for fast lookups by key.

**Example:**
```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
```

- **Mutability:** Mutable - Key-value pairs can be added, removed, or updated.
- **Time Complexity:**
    - Accessing/Searching/Inserting/Deleting: O(1)
- **Strengths:**
    - Efficient key-based lookup and retrieval.
    - Flexible: Can store any type of data as values.
- **Weaknesses:**
    - Unordered: Does not inherently maintain insertion order (though, CPython 3.7+ maintains it for iteration).
    - Keys must be hashable (immutable types like strings, numbers, tuples).

### 3. Tuples:

**Definition:** An ordered, immutable collection of items. Tuples are similar to lists, but their elements cannot be changed after creation.

**Example:**
```python
my_tuple = (10, 20, "Python")
```

- **Mutability:** Immutable - Cannot be modified after creation.
- **Time Complexity:**
  - Similar to lists for accessing and searching: O(1) and O(n) respectively.
- **Strengths:**
    - Data integrity: Immutability ensures data consistency.
    - Can be used as dictionary keys (due to immutability).
- **Weaknesses:**
    - Cannot be modified once created.
    - Less versatile than lists due to immutability.

### 4. Sets:

**Definition:** An unordered collection of unique elements.

**Example:**
```python
my_set = {1, 2, 3, 2, 1}  # Results in {1, 2, 3}
```

- **Mutability:** Mutable - Elements can be added and removed.
- **Time Complexity:**
    - Accessing element: O(1) (using `in` operator)
    - Inserting/Deleting: O(1)
    - Union, Intersection: O(len(s) + len(t)) where s and t are the sets involved.
- **Strengths:**
    - Eliminates duplicate elements.
    - Supports set operations like union, intersection, difference.
- **Weaknesses:**
    - Unordered: Elements are not stored in a specific order.
    - Cannot store mutable objects like lists or dictionaries as elements.

### 5. Frozen Sets:

**Definition:** An immutable version of a set. Once created, elements cannot be added or removed.

**Example:**
```python
my_frozen_set = frozenset([1, 2, 3])
```

- **Mutability:** Immutable - Cannot be modified after creation.
- **Time Complexity:** Similar to sets.
- **Strengths:**
    - Can be used as dictionary keys (due to immutability).
    - Data integrity: Immutability ensures data consistency.
- **Weaknesses:**
    - Cannot be modified after creation.

### 6. Strings:

**Definition:** An ordered, immutable sequence of characters, used to represent text.

**Example:**
```python
my_string = "Hello, world!"
```

- **Mutability:** Immutable - Cannot be modified in place.
- **Time Complexity:**
    - Accessing element: O(1)
    - Concatenation: O(n) where n is the length of the concatenated string.
    - Searching substring: O(n*m) in worst case (`naïve approach`), where n is the length of the string and m is the length of the substring.
- **Strengths:**
    - Widely used for text manipulation and representation.
    - Rich set of built-in methods for string operations.
- **Weaknesses:**
    - Immutability leads to the creation of new string objects during modifications.

### 7. Bytearrays:

**Definition:** A mutable sequence of bytes (integers ranging from 0 to 255), typically used for handling binary data.

**Example:**
```python
my_bytearray = bytearray(b"Hello")
```

- **Mutability:** Mutable - Elements (bytes) can be modified after creation.
- **Time Complexity:**
    - Accessing/Modifying element: O(1)
- **Strengths:**
    - Useful for working with binary data, network programming, and low-level operations.
    - Mutable, allowing modification of individual bytes.
- **Weaknesses:**
   -  Specific use cases, not as commonly used as strings for general text.
   - **Why use bytearrays when we can store byte values in lists?** Bytearrays are more memory-efficient and faster for binary data operations as they store bytes directly, while lists store object references. Bytearrays also integrate better with low-level interfaces that work with raw byte buffers.

## Collections Module

The `collections` module extends Python's built-in data structures, providing specialized containers with enhanced functionality.

### Counter

Counter are dictionaries that count hashable objects.

**Example:**
```python
from collections import Counter

my_list = [1, 2, 1, 3, 2, 1, 4]
my_counter = Counter(my_list)
print(my_counter)  # Output: Counter({1: 3, 2: 2, 3: 1, 4: 1})
```

### OrderedDict

OrderedDict preserve the order in which elements were inserted, unlike regular dictionaries.

**Example:**
```python
from collections import OrderedDict

my_ordered_dict = OrderedDict()
my_ordered_dict["a"] = 1
my_ordered_dict["b"] = 2
print(my_ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2)])
```

### DefaultDict

DefaultDict automatically assign a default value to keys that haven't been seen before.

**Example:**
```python
from collections import defaultdict

my_default_dict = defaultdict(int)
my_default_dict["a"] += 1
print(my_default_dict["a"])  # Output: 1
```

### ChainMap

ChainMap combine multiple dictionaries into a single, updatable view.

**Example:**
```python
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
my_chain_map = ChainMap(dict1, dict2)
print(my_chain_map["b"])  # Output: 2
```

### NamedTuple

NamedTuple assign names to each position in a tuple, enhancing readability and usability.

**Example:**
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
my_point = Point(10, 20)
print(my_point.x)  # Output: 10
```

### Deque

Deque are double-ended queues, optimized for appending and popping elements from both ends.

**Example:**
```python
from collections import deque

my_deque = deque([1, 2, 3])
my_deque.append(4)
my_deque.appendleft(0)
print(my_deque)  # Output: deque([0, 1, 2, 3, 4])
```

### UserDict

`UserDict` is a class that acts as a wrapper around a dictionary object. It's designed to let you subclass the dict type and easily customize its behavior.

**Example:**
```python
from collections import UserDict

class MyDict(UserDict):
    def __init__(self, data=None, **kwargs):
        super().__init__(data, **kwargs)
        self.history = []

    def __setitem__(self, key, value):
        self.history.append((key, value))
        super().__setitem__(key, value)

my_dict = MyDict()
my_dict["a"] = 1
my_dict["b"] = 2
print(my_dict.history)  # Output: [('a', 1), ('b', 2)]
```

### UserList

`UserList` is similar to `UserDict`, but it wraps around a list object instead. This allows you to create custom list-like classes with modified behavior.

**Example:**
```python
from collections import UserList

class MyList(UserList):
    def __init__(self, data=None):
        super().__init__(data)

    def append(self, item):
        self.data.append(item.upper())

my_list = MyList(["a", "b"])
my_list.append("c")
print(my_list)  # Output: ['a', 'b', 'C']
```

### UserString

`UserString` provides a mutable wrapper around string objects. You can inherit from this class to create your own string-like objects with custom methods and properties.

**Example:**
```python
from collections import UserString

class MyString(UserString):
    def reverse(self):
        return self[::-1]

my_string = MyString("hello")
print(my_string.reverse())  # Output: olleh
```

These "User" classes in the `collections` module offer a powerful way to extend Python's built-in data structures and tailor them to your specific needs.
