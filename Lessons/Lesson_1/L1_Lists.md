# Lists  

Lists are by far the most used data structure in Python, so we will spend a bit more time on them.

The ``list`` type in Python is used to store multiple items (objects) in  a single variable.

We have already seen them in use, but here is a quick example:

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]
```

This is a list of strings which has 5 items. If you need convincing that this is a list type, then you can use ``type(car_list)`` to check the type.

Lists are hetrogeneous, which is a fancy way of saying we can store different data types. They can also store duplicates e.g.

```python
car_list = ["Volvo", 1, False, "Ford", "Ford", False, 3.14]
```

This list has both different types and duplicates.

## 1. List Items

Each object in the list is called an item (element). We will use the previous example to demonstrate simple operations on lists. 

If you want to follow along then type this into the Python interactive shell.

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]
```

### 1.1 Access List Items

You can access a list item by it's index. Python indexing starts at ``0``, so to get the first item of a list you would use.

For example we can print the first item using,

```python
print(car_list[0]) # prints out Volvo
```

or the third item by using:

```python
car_list[2] # prints out Honda
```

Notice how the ``car_list`` has ``5`` items. So it's indexing goes from ``0-4``.

If you try typing,

```python
car_list[5] # IndexError
```

you will get an ``IndexError`` because your list index if not in the valid range ``0-4``.

#### 1.1.1 Slicing

You can also access slices (portions) of a list. For example we can access items 1,2,3 using:

```python
print(car_list[1:4]) # prints ["Volvo", "Audi", "Honda"]
```

#### 1.1.2 Negative Indices

You can also access from the back of the list. To get the last item use ``-1``.

```python
print(car_list[-1]) # prints ["Mercedes"]
```

You can also get slices such as the last three items.

```python
print(car_list[-4,-1]) # prints ["Honda", "Ford", "Mercedes"]
```
### 1.2 Changing List Items
You change a list item using indexing as follows:

```python
car_list[2] = "Ferrari"
```

If we print out the list,

```python
print(car_list) # prints ["Volvo", "Audi", "Ferrari", "Ford", "Mercedes"]
```

you will get ``['Volvo', 'Audi', 'Ferrari', 'Ford', 'Mercedes']``.

### 1.3 Adding List Items

You can add to a list by using the ``append()`` and ``insert()``  methods.

Methods are very much like functions, they take in arguments and return something. Hey, they even look like them!

The key difference is a method is attached to an object and you call the method using dot notation. 

To add to the end of the list use ``append()`` method. Note that it is called using a ``.``:

```python 
car_list.append("Skoda") # ["Volvo", "Audi", "Ferrari", "Ford", "Mercedes", "Skoda"]
```

Here the ``str`` ``"Skoda"`` is added to the end of the list.

To insert an item somewhere use the ``insert()`` method, you supply the index as the first parameter and the item as the second.

```python 
car_list.insert(2, "Porsche") # insert "Porsche" at index 2, i.e. 3rd item 
# ["Volvo", "Audi", "Porsche", "Ferrari", "Ford", "Mercedes", "Skoda"]
```

### 1.4 Extending and Joining Lists

To extend the list by multiple items you can use either the ``extend()`` method or the ``+`` operator.

```python 
list_one = ["a", "b" , "c"]
list_two = [1, 2, 3]
list_one.extend(list_two) # list_one now contains ["a", "b", "c", 1, 2, 3]
```

```python 
list_one = ["a", "b" , "c"]
list_two = [1, 2, 3]
list_three = list_one + list_two # list_three contains ["a", "b", "c", 1, 2, 3]
```

Note the difference, the ``extend()`` method extends the list it is operating on (e.g. ``list_one``). The ``+`` operator creates a new list by joining the lists, we stored this in ``list_three``.

We can use the ``+`` operator to join many lists.

```python 
list_one = ["a", "b" , "c"]
list_two = [1, 2, 3]
list_three = [True, False]
list_four = list_one + list_two + list_three # list4 contains ["a", "b", "c", 1, 2, 3, True, False]
```

### 1.5 Remove List Items

Again working on the car example:

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]
```

You can remove a list item using either ``remove()`` or ``pop()`` methods, or the ``del`` keyword.

***

``remove()`` lets you remove an item by specifying the value of the item, .e.g.
```python
car_list.remove("Audi") # removes the second item of the list 
```

If you try to remove an object that isn't in the list you will get a ``ValueError``. For example

```python
car_list.remove("Ferrari") # ValueError: list.remove(x): x not in list
```

Note that this returns ``None``. This is demonstrated by this code snippet.

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]
item_removed = car_list.remove("Audi")
print(car_list) # prints ["Volvo", "Honda", "Ford", "Mercedes"]
print(item_removed) # prints None
```

Here we stored the ``return`` value  of ``remove()`` in ``item_removed`` which was ``None``.

***

``pop()`` lets you remove an item by index, e.g.

```python
car_list.pop(1) # removes the second item of the list
```

Note that this returns the item that is removed from the list. This is demonstrated by this code snippet.

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]
item_removed = car_list.pop(1)
print(car_list) # prints ["Volvo", "Honda", "Ford", "Mercedes"]
print(item_removed) # prints Audi
```

***

The ``del`` keyword also lets you remove by index, e.g.

```python
del car_list[1] # removes the second item of the list
```

We can also remove slices.

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]
del car_list[1:3]
print(car_list) # prints ["Volvo", "Ford", "Mercedes"]
```

### 1.6 Note on In-place Methods
All the methods we have seen operating on a list are known as an in-place method as they update the list directly. We will discuss this more in the next lesson.

Also be careful with understanding what a method returns. If you tried the following,

```python
print(car_list.append("Renault")) # prints None
```

it will update the list, but print the ``return`` value which is ``None``.

## 2. List Methods

There are a number of built-in list methods you can use:

| Method | Description |
--- | ---|
| ``append()``	| Adds an element at the end of the list |
| ``clear()`` |	Removes all the elements from the list |
| ``copy()``	| Returns a copy of the list |
| ``count()``	 | Returns the number of elements with the specified value |
| ``extend()`` |	Add the elements of a list (or any iterable), to the end of the current list |
| ``index()`` |	Returns the index of the first element with the specified value |
| ``insert()`` |	Adds an element at the specified position |
| ``pop()``	| Removes the element at the specified position |
| ``remove()`` |	Removes the item with the specified value |
| ``reverse()``	| Reverses the order of the list |
| ``sort()`` | Sorts the list |

For example we can sort the list as follows:

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]

car_list.sort() # in-place operation, sorts car_list

print(car_list) # prints ['Audi', 'Ford', 'Honda', 'Mercedes', 'Volvo']

```

## 3. Looping Through a List

You can loop through a list using a ``for`` loop.

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]

for car in car_list:
    print(car)

# prints out...
# Volvo
# Audi
# Honda
# Ford
# Mercedes
```

We can also loop through a list using a ``while`` loop.

```python
car_list = ["Volvo", "Audi", "Honda", "Ford", "Mercedes"]

i = 0
while i < len(car_list):
    print(car_list[i])
    i += 1

# prints out...
# Volvo
# Audi
# Honda
# Ford
# Mercedes
```

### 3.1. List of lists

We can also have lists of lists. These are very common and you will need to now how to iterate (loop) over them

Here is an example that just iterates over the list and prints out each of the sublists.
```python
list_one = [[4,2,6], [3,8,3], [5,4,7]]
for sub_list in list_one:
    print(sub_list)

# prints out...
# [4,2,6]
# [3,8,3]
# [5,4,7]
```

As each of the sublists is a list, we can iterate over each of these.

```python
list_one = [[4, 2, 6], [3, 8, 3], [5, 4, 7]]
for sub_list in list_one:
    for x in sub_list:
        print(x)
# prints out...
# 4
# 2
# 6
# 3
# 8
# 3
# 5
# 4
# 7

```
We can even write a simple program that gives us back a list of the total of each sublist. Here we create an empty list called ``sum_list`` and then we compute the total of each sublist and store it in the ``sum_list``.
```python
list_one = [[4, 2, 6], [3, 8, 3], [5, 4, 7]]

sum_list = []

for sub_list in list_one:
    total = 0
    for x in sub_list:  # iterate over the sub_list
        total += x  # keep adding items in the sub_list to total

    sum_list.append(total)  # append the result to sum_list

print(sum_list)  # prints [12,14,16]
```

### 3.2. Zipping Two Lists

Zipping lists together is a very useful thing to do when we want to combine lists together and loop over them.

The zip operation is demonstrated by the following code snippet. Note both must be the same length.

```python
list_one = [1,2,3]
list_two = ["a","b","c"]

for x,y in zip(list_one, list_two):
    print(x,y)

# prints
# 1 a
# 2 b
# 3 c
```

*** 
# === TASK ===
Create two functions.

Your first function should be called ``longest_word`` which takes in a list of a list of strings and returns the longest word in any of the lists. In the case of equal length words, return the first word you encounter.

For example:

```python
longest_word([["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]) # return revolution
```

The second should be called ``num_characters`` which takes in a list of a list of strings and returns the total number of characters in all of the strings in the list lists.

```python
num_characters([["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]) # return 105
```

Copy the following into **main.py** to get started.

```python
def longest_word(string_list):
    pass # placeholder, delete and replace with your code
  
def num_characters(string_list):
    pass # placeholder, delete and replace with your code
  
if __name__ == "__main__":
    test_string = [["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]
    test_string2 = [["Hello", "World"], ["Apple", "Pears"]]
    print(longest_word(test_string)) # should print revolution
    print(num_characters(test_string)) # should print 105
    print(longest_word(test_string2)) # should print hello
    print(num_characters(test_string2)) # should print 20
```

***

# References 

[Python List Methods - W3schools](https://www.w3schools.com/python/python_lists_methods.asp)