# Dictionaries  

Dictionaries are a very common in Python are used to store key:value pairs.

In other languages these might be called something else such as a HashMap.

Dictionaries are:

1. Indexed by Key
2. Mutable (changeable)
3. Hetrogeneous 
   
By **indexed by key** we mean that each value that we store in the dictionary has a unique key that allows you to access it.

By **mutable** we mean that the items in the dictionary can be changed and we can add/remove key:value pairs

By **hetrogeneous** we mean that we can mixed different data types for the key:value pairs.

Here is a quick example:

```python
student_dict = {
    1123425: "Ada Lovelace",
    1425243: "Melba Roy Mouton",
    1512414: "Alan Turing"
}
# stores student names by their id.
# Here key:value pair is id: name
```
Here is another example using different types as keys and values.

```python
test_dict = {
    1: "Hello World",
    "Test": False,
    "Another Key":[1,2,3,4]
}
```

The only issue here is that keys need to be a hashable type. For now that means don't use a list as a key.

A good analogy to remember dictionaries is well, a dictionary. In a dictionary you look up a word (key) and you can get the corresponding description (value)

## 1. Dictionary Items
Let's use the ``student_dict`` as our example.

```python
student_dict = {
    1123425: "Ada Lovelace",
    1425243: "Melba Roy Mouton",
    1512414: "Alan Turing"
}
# stores student names by their id.
# Here key:value pair is id: name
```

### 1.1 Access Dictionary Items

We can access a dictionary item using the key name inside square brackets.

```python
print(student_dict[1123425]) # prints "Ada Lovelace"
```

When accessing the item using the key name, it returns the corresponding value.

### 1.2 Change Dictionary Items

We can change a dictionary item using the key name inside square brackets.

```python
student_dict[1123425] = "Guido van Rossum" # changes the value from "Ada Lovelace" to "Guido van Rossum"

print(student_dict) 
# {1123425: 'Guido van Rossum', 1425243: 'Melba Roy Mouton', 1512414: 'Alan Turing'}
```
### 1.3 Add Dictionary Items
To add an item to a dictionary you again use the key name with square brackets

It is essentially the same as changing an item, but the key isn't yet in the dictionary.

```python
student_dict[1234567] = "Margaret Hamilton" # adds the key:value pair to the dictionary

print(student_dict) 
# {1123425: 'Guido van Rossum', 1425243: 'Melba Roy Mouton', 1512414: 'Alan Turing', 1234567: 'Margaret Hamilton'}
```
### 1.4 Remove Dictionary Items

You can remove a dictionary item by using the ``del`` keyword.

```python
del student_dict[1425243] # removes the 1425243: "Melba Roy Mouton" 

print(student_dict) 
# {1123425: 'Guido van Rossum', 1512414: 'Alan Turing', 1234567: 'Margaret Hamilton'}
```

## 2. Types of Dictionary Keys

Anything that is immutable can be a dictionary key. e.g., ``int``, ``str``, ``float``. 

```python
dictionary1 = {
    1: 100,
    2: 300,
    42: 250
}

dictionary2 = {
    "Abid": 100,
    "Fatima": 300,
    "Sam": 250
}
```

We can also use a tuple as a key.

```python
dictionary3 = {
    (1,10): 100,
    (11,20): 300,
    (21,30): 250
}
```

You can access an item using the tuple or the values of the tuple.

```python
print(dictionary3[(1,10)])	# print 100
print(dictionary3[1,10])	# print 100
```

You can have mixed immutable types in your tuple, e.g.

```python
dictionary4 = {
    (1,'a'): 100,
    (1,'b'): 300,
    (1,'c'): 250
}

print(dictionary4[1,'a'])	# print 100
print(dictionary4[1,'b'])	# print 300
```

### 2.1 Lists Aren't Allowed (Mutable)

```python
dictionary4 = {
    [1,'a']: 100,
    [1,'b']: 300,
    [1,'c']: 250
}
```

This will cause an error! 

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    dictionary4 = {
TypeError: unhashable type: 'list'
```

The reason is that lists are mutable, hence can be changed. A key should never change otherwise how do you access it if you don't know the key. The error is saying we can't hash the type, meaning we can't create a unique identifier in memory because it might change.

Yes you could track it but this would be a bad idea. Just don't let it change!

## 3. Looping Through a Dictionary

You can loop through a dictionary in a number of ways. 

If you want to loop through the keys you can do the following.

```python
student_dict = {
    1123425: "Ada Lovelace",
    1425243: "Melba Roy Mouton",
    1512414: "Alan Turing"
}
for key in student_dict.keys():
    print(key)

# prints...
# 1123425
# 1425243
# 1512414
```

You can also use this to get the values:

```python
for key in student_dict.keys():
    print(f"Key = {key}, Value = {student_dict[key]}")

# prints...
# Key = 1123425, Value = Ada Lovelace
# Key = 1425243, Value = Melba Roy Mouton
# Key = 1512414, Value = Alan Turing
```

Another way, perhaps the most common is using the ``items()`` method.

```python
for k, v in student_dict.items():
    print(f"Key = {k}, Value = {v}")
```

Here ``items`` returns a list (actually a type called ``dict_items``) of (``key``, ``value``) pairs that you can then bind to the variables ``k`` and ``v`` for each iteration of the loop.

### 3.1 Looping Through a Dictionary with Tuple Keys

We can also loop over a dictionary with ``tuple`` keys.

```python
dictionary4 = {
    (1,'a'): 100,
    (1,'b'): 300,
    (1,'c'): 250
}

for key, value in dictionary4.items():
    print(key)
    print(value)
```

Or to access the first and second items of the key individually.

```python
for key, value in dictionary4.items():
    print(key[0])
    print(key[1])
    print(value)
```

## 4. Nested Dictionaries

Nested dictionaries are extremely useful.

For example we might want to store lots of information about each student. Let's store their email as well as their name.

```python
student_dict = {
    1123425: {
        "Name":  "Ada Lovelace",
        "Email": "a.lovelace@unimail.derby.ac.uk"
    },
    1425243: {
        "Name":  "Melba Roy Mouton",
        "Email": "m.mouton@unimail.derby.ac.uk"
    },
    1512414: {
        "Name":  "Alan Turing",
        "Email": "a.turing@unimail.derby.ac.uk"
    }
}
# stores student names by their id.
# Here key:value pair is id: {information dictionary}
```

Now if you want information about a student you can get the corresponding dictionary.

```python
student1 = student_dict[1123425] # returns {"Name":  "Ada Lovelace", "Email": "a.lovelace@unimail.derby.ac.uk" }
print(student1["Name"]) # prints 'Ada Lovelace'
print(student1["Email"]) # prints a.lovelace@unimail.derby.ac.uk
```

You can access the email in one line if you like.

```python
print(student1[1123425]["Email"]) # prints a.lovelace@unimail.derby.ac.uk
```

## 5. Copying a Dictionary
  
Just like a list, copying a dictionary is stickier than you might imagine!

Dictionaries are also stored using references. 

The variable stores the dictionary location in memory.

```python
dict1 = {"a":1, "d":4}
dict2 = dict1 # copies the reference to dict1
print(f"Dictionary 1 = {dict1}")
print(f"Dictionary 2 = {dict2}")
dict2["c"] = 3
print(f"Dictionary 1 = {dict1}") # prints {'a':1, 'd':4, 'c':3}
print(f"Dictionary 2 = {dict2}") # prints {'a':1, 'd':4, 'c':3}
```

The above copies the reference to the list object. We can check this by using the ``id()`` function.

```python
id(dict1) # something like 140094119425920
id(dict2) # will be the same id as above 140094119425920
```

To copy a dictionary we must use the ``copy()`` method.

```python
dict1 = {"a":1, "d":4}
dict2 = dict1.copy() # copies the reference to dict1
print(f"Dictionary 1 = {dict1}") # prints {'a':1, 'd':4}
print(f"Dictionary 2 = {dict2}") # prints {'a':1, 'd':4}
dict2["c"] = 3
print(f"Dictionary 1 = {dict1}") # prints {'a':1, 'd':4}
print(f"Dictionary 2 = {dict2}") # prints {'a':1, 'd':4, 'c':3}
```

Now you will see that ``dict1`` is not updated when you add to ``dict2``.

Again we can check using the ``id()`` function if they point to the same location:

```python
id(list1) # something like 140094119425920
id(list2) # will be a different id e.g. 140094117695872
```

## 6. Dictionary Methods

There are a number of built in methods you can use on a dictionary. You have already seen ``keys()`` and ``items()``

| Method | Description |
| --- | --- |
|``clear()``| Removes all the elements from the dictionary |
|``copy()``|	Returns a copy of the dictionary |
|``fromkeys()``|	Returns a dictionary with the specified keys and value |
|``get()``|	Returns the value of the specified key |
|``items()``|	Returns a list containing a tuple for each key value pair |
|``keys()``|	Returns a list containing the dictionaries keys |
|``pop()``|Removes the element with the specified key |
|``popitem()``|	Removes the last inserted key-value pair |
|``setdefault()``|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
|``update()`` |	Updates the dictionary with the specified key-value pairs |
|``values()`` |	Returns a list of all the values in the dictionary |

[Python Dictionaris - W3schools](https://www.w3schools.com/python/python_dictionaries.asp)

*** 
# === TASK ===

The function ``add_from_list()``, should take in a dictionary and a list of tuples and then add these as key value pairs to the dictionary. It should not return anything.

For example,
```python
test_dict = {
    "a":1,
    "b":2
}
print(test_dict) # prints {'a':1, 'b':2}
items_to_add = [("e", 5), ("z", 26)]
add_from_list(test_dict, items_to_add)
print(test_dict) # prints {'a':1, 'b':2, 'e':5, 'z':26}
```

HINT: You can loop through a list of paired values as follows. You might want to try this code out if you don't quite understand it.
```python
for x,y in [(1,2), (5,1), (2,3)]:
    print(x,y)
```

Copy the following into **main.py** to get started.

```python
def add_from_list(d, items_to_add):
    pass
  
if __name__ == "__main__":
    test_dict = {
        "a":1,
        "b":2
    }
    print(test_dict) # prints {'a':1, 'b':2}
    items_to_add = [("e", 5), ("z", 26)]
    add_from_list(test_dict, items_to_add)
    print(test_dict) # prints {'a':1, 'b':2, 'e':5, 'z':26}
```
***

# References

[Python Dictionaries - W3schools](https://www.w3schools.com/python/python_dictionaries.asp)