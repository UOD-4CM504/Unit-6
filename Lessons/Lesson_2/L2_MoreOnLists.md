# More on Lists  

Please carefully read this lesson, it is very important!

I highly recommend you copy and paste code snippets into [Python Tutor](https://pythontutor.com/).

It visualises what is happening and will really aid your understanding!

## 1. Copy and Deep Copy

### 1.1. Copying a List

Copying a list is a bit stickier than you might imagine!

Lists are stored using some things called references. 

The variable (name) stores the list location in memory.

```python
list1 = [1,2,3]
list2 = list1 # copies the reference to list1
print(f"List 1 = {list1}")
print(f"List 2 = {list2}")
list2.append(4) # this will update both list1 and list2
print(f"List 1 = {list1}") # prints [1,2,3,4]
print(f"List 2 = {list2}") # prints [1,2,3,4]
```

The above copies the reference to the list object. We can check this by using the ``id()`` function.

```python
id(list1) # something like 140416978254080
id(list2) # will be the same id as above 140416978254080
```

To copy a list we use the ``copy()`` method.

```python
list1 = [1,2,3]
list2 = list1.copy() # copies the list to a new object and store
print(f"List 1 = {list1}")
print(f"List 2 = {list2}")
list2.append(4) # this will update both list1 and list2
print(f"List 1 = {list1}") # prints [1,2,3]
print(f"List 2 = {list2}") # prints [1,2,3,4]
```

Now you will see that ``list1`` is not updated when you append to ``list2``.

Again we can check this with:

```python
id(list1) # something like 140416978254080
id(list2) # will be a different id e.g. 140404308187456
```


### 1.2. Deep Copying a List

There is a caveat. When we have a list of lists, the ``copy()`` method will create copies of the lists, but not new copies of the items in the list.

Again, I strongly suggest that you copy this into [Python Tutor](https://pythontutor.com/) and visually understand what is happening.

For example,

```python
demo_list = [[1],2,3]
copy_list = demo_list.copy()

print(id(demo_list)) # these ids will be different
print(id(copy_list))

# print item 1 ids
print(id(demo_list[0])) # these ids are the same
print(id(copy_list[0]))

# print item 2 ids
print(id(demo_list[1])) # these ids are the same
print(id(copy_list[1]))

# print item 3 ids
print(id(demo_list[2])) # these ids are the same
print(id(copy_list[2]))
```

Because the item at index 0 is actually a list and is mutable (see the next section). Changing the items in this list will be reflected in both the orginal list and the copy of the list.


For example,

```python
demo_list = [[1],2,3]
copy_list = demo_list.copy() # do a shallow copy

demo_list[0][0] = "Sam" # change the first item in the first item (this is a list)

print(demo_list) # prints [["Sam"],2,3]
print(copy_list) # prints [["Sam"],2,3]
```
Yikes, this updated both lists! Be careful.

To fix this you can use the ``deepcopy()`` function. You will need to import the copy module.

```python
import copy
demo_list = [[1],2,3]
copy_list = copy.deepcopy(demo_list) # do a deep copy

demo_list[0][0] = "Sam" # change the first item in the first item (this is a list)

print(demo_list) # prints [["Sam"],2,3]
print(copy_list) # prints [[1],2,3]
```

Try running the above code in [Python Tutor](https://pythontutor.com/) to get a better understanding of this.

## 2. Immutable vs Mutable
Python differs from other programming languages in that everything is an object.

Some of these objects are immutable (cannot be changed) and some are mutable (can be changed).

Immutable and mutable types are common in most languages and how these are dealt with differs. 
### 2.1. Immutable Types
An immutable type is something that once created cannot be changed. Immutable types you have seen in Python are ``str``, ``float``, ``int`` and ``bool``.

Consider the following example which uses ``int``. Here we also use the ``is`` keyword to see if ``x`` and ``y`` are the same object in memory.

```python
x = 1
y = x
print(x is y) # prints True. They are the same object in memory

y += 1
print(x) # prints 1
print(y) # prints 2
print(x is y) # prints False. They are now different objects in memory
```
The first ``print(x is y)`` prints ``True`` because ``x`` and ``y`` are both attached to the same immutable object ``1``.

The reason the second ``print(x is y)`` prints ``False`` is because to start with ``x`` and ``y`` are attached to the immutable object ``1``; however, when we add ``1`` to ``y`` Python creates a new object and reassigns ``y`` to ``2``.

Now ``x`` points to the object ``1`` in memory and ``y`` points to the object ``2`` in memory. Different objects!

### 2.2. Mutable Types
Lists are mutable. If we do something similar to the above we get a very different result.

Consider the following example which uses ``list``. Here we also use the ``is`` keyword to see if ``list_one`` and ``list_two`` are the same object in memory.
```python
list_one = [1,2,3]
list_two = list_one
list_two.append(4)

print(list_one) # prints [1,2,3,4]
print(list_two) # prints [1,2,3,4]
print(list_one is list_two) # prints True. They are the same object in memory
```
When we assign ``list_two = list_one`` both names are pointing to the same object ``[1,2,3]`` in memory.

When we call the append method, we add ``4`` to the end of the list ``[1,2,3]``. Both ``list_one`` and ``list_two`` still point to the same list which is now ``[1,2,3,4]``. Hence ``print(list_one is list_two)`` prints ``True``.

We can stop this from happening by using a copy.

Here we assign ``list_two`` to a copy of the object ``[1,2,3]`` in memory. This now means that ``list_one`` points to one object ``[1,2,3]`` and ``list_two`` points to a separate object ``[1,2,3]``.
```python
list_one = [1,2,3]
list_two = list_one.copy() # now we create a copy 
list_two.append(4) 

print(list_one) # prints [1,2,3]
print(list_two) # prints [1,2,3,4]
print(list_one is list_two) # prints False. They are now different objects in memory
```
The ``append()`` method is now only called on the object attached to ``list_two`` and therefore the object attached to ``list_one`` is not updated. Hence ``print(list_one is list_two)`` prints ``False``.


## 3. Passing by Assignment

**WARNING: This is really fundamental and can cause major bugs and errors if you don't understand it.**

This section is repeated from Unit 5, but it is so fundamental I want to present it again.

When we pass arguments to functions, what we are actually doing is binding objects to the parameters of the function.

### 3.1 Passing an Immutable Type

In Python, a variable is just a name (label) that can be attached to an object. When we pass an object to a function, the function parameter is attached to the passed object

In the example below ``x`` will be attached to whatever is passed into the function ``add_one()``. If you pass in an immutable object, as soon as you try to update the object it will create a new object to reflect the changes.

Remember immutable objects can't be changed. 

The following example illustrates this. We pass in a number that is attached to ``num`` and then add ``1``. Because we are trying to change an immutable object, we have to create a new object. However, we don't return anything and reassign, so the original variable ``num_one`` is not changed.
```python
def add_one(num):
    num += 1 # add one to the local variable x

num_one = 1
print(num_one) # prints 1 
add_one(num_one)
print(num_one) # prints 1
```

We can reflect the changes by returning the result and reassigning it to ``num_one``.
```python
def add_one(num):
    num += 1
    return num # return the new object created by adding 1

num_one = 1
print(num_one) # prints 1
num_one = add_one(num_one) # reassign x1 to the result of add_one()
print(num_one) # prints 2
```

### 3.2 Passing a Mutable Type

Try running the code snippets in [Python Tutor](https://pythontutor.com/) to get a better understanding of the following.

When you pass a mutable object to a function and change it you are updating the original object. That is, doing something to the object passed to the function doesn't create a new copy, it operates on the same object!

Here is a simple example that adds ``4`` to the end of a list.

```python
def func_one(items):
    """ append 4 to the list. """
    # append adds to the end of the list
    items.append(4)

list_one = [1, 2, 3]
func_one(list_one) # call func_one with list_one
print(list_one) # prints [1,2,3,4] - this has been updated by the function call
```

The object attached to variable ``list_one`` is first passed to ``func_one()`` and the variable ``items`` is attached to the object. 

The function then adds ``4`` to the end of the list using the ``append()`` method. What happens here is both ``list_one`` and ``items`` point to the mutable list. When it is updated, both are updated as they point to the same object.

Below are some more examples that illustrate passing a list to a function.

```python
def func_one(items):
    """append 4 to the list."""
    # append adds to the end of the list
    items.append(4)

def func_two(items):
    """add the list and [4]"""
    # this creates a new object by adding the lists items and [4]
    items = items + [4]

def func_three(items):
    """add the list and [4]"""
    # again this creates a new object by adding the lists items and [4]
    items = items + [4]
    # however this time we return the new object
    return items

list_one = [1, 2, 3]
func_one(list_one)  # call func_one with list_one
print(list_one)  # prints [1,2,3,4] - this has been updated by the function call

list_one = [1, 2, 3]
func_two(list_one)  # call func_two
print(list_one)  # prints [1,2,3] - this has not been updated by the function call

list_one = [1, 2, 3]
list_two = func_three(list_one)  # call func_three and bind to the variable list_two
print(list_two)  # prints [1,2,3,4] - the new object created by the function call
```

``func_one()`` operates on the original list, this means you don't need to return anything. You could choose to return the list here, but there is no point. 

``func_two()`` adds the original list and the list ``[4]``. This creates a new list but we do not return it and therefore we lose the new list.

``func_three()`` adds the original list and the list ``[4]``. This creates a new list and we return it. This means we can use it outside of our function.

I would experiment with these in [Python Tutor](https://pythontutor.com/) to make sure you understand what is going on.

### 3.3 To Return or Not To Return

Generally, if you are operating on a mutable object and you don't need to keep a copy of the original then there is no need to return anything.

If you need the original list intact then you need to copy the original list before you operate on it and return the modified copy. Review Section 1 on Copy and Deep Copy.

*** 
# === TASK ===
In **main.py** there is a function called ``change_list()`` that you need to update.

The function should remove the second item, add "Banana" to the list and then sort the list. 

The function should return the modified list without affecting the original list.

An example of how the function should work is given below.
```python
fruit_list = ["Pear", "Orange", "Peach", "Apple"]
print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
new_fruit_list = change_list(fruit_list)
print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
print(new_fruit_list) # prints ["Apple", "Banana", "Peach", "Pear"]
```

Copy the following into **main.py** to get started.
```python
def change_list(my_list):
    pass

if __name__ == "__main__":
    fruit_list = ["Pear", "Orange", "Peach", "Apple"]
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    new_fruit_list = change_list(fruit_list)
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    print(new_fruit_list) # prints ["Apple", "Banana", "Peach", "Pear"]
```
***