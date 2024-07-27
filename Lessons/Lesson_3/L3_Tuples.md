# Tuples

Tuples are very similar to lists but differ in a two key ways. Tuples are:

1. Ordered
2. Immutable (unchangeable)

By **ordered** we mean that the tuple has an order and it cannot be changed.

By **immutable** we mean that the tuple cannot be added to, removed from and items cannot be changed.

You define a tuple in much the same way as a list, but with round brackets, not square.

```python
car_tuple = ("Audi", "Mercedes", "Ferrari")
```

## 1. Tuple Items

You can access tuple items using indexing, e.g.

```python
print(car_tuple[1]) # prints the 2nd item of the tuple, "Mercedes"
```

You can also use slicing and negative indexing as per lists.

```python
print(car_tuple[0:2]) # prints the 1st and 2nd items of the tuple, ("Audi", "Mercedes")
print(car_tuple[-1]) # prints the last item of the tuple, "Ferrari"
```

## 2. Looping Through a Tuple

You can loop through a tuple just like a list using a ``for`` loop.

```python
car_tuple = ("Audi", "Mercedes", "Ferrari")

for car in car_tuple:
    print(car)

# prints..
# Audi
# Mercedes
# Ferrari
```

You can also use a while loop.

```python
car_tuple = ("Audi", "Mercedes", "Ferrari")

i = 0
while i < len(car_tuple):
    print(car_tuple[i])
    i += 1

# prints..
# Audi
# Mercedes
# Ferrari
```

## 3. Unpacking a Tuple

It is often useful to unpack a tuple. This allows you to bind each item of a tuple to a variable.

```python
car_tuple = ("Audi", "Mercedes", "Ferrari")
(x,y,z) = car_tuple # binds x = "Audi", y = "Mercedes" and z = "Ferrari"
```

### 3.1. Function Return Values
At first you might think what the point of this is. It comes in very handy in a few circumstances. One of the main ones is with function return values.

Remember that a function can only return one object, but it can return a tuple!

Suppose that we want a function to computer the sum, average and the length of a list.
```python
def num_list_stats(num_list):
    len_list = len(num_list)
    sum_list = sum(num_list)
    avg_list = sum_list/len_list
    return (sum_list, avg_list, len_list)

# main code
test_list = [1,64,71,-3]
(test_sum, test_avg, test_len) = num_list_stats(test_list) # call function and bind return tuple
print(f"Sum of list is {test_sum}")
print(f"Average of list is {test_avg}")
print(f"Length of list is {test_len}")
```

In the code above ``num_list_stats`` takes a list and then computes the sum, average and length of the list and returns these as a 3-tuple.

The calling code unpacks this and binds it to the variables ``test_sum``, ``test_avg`` and ``test_len``.

Note that you can do it without the brackets, and it looks like it is returning 3 things, it isn't it is still just a returning a ``tuple``. 

```python
def num_list_stats(num_list):
    len_list = len(num_list)
    sum_list = sum(num_list)
    avg_list = sum_list/len_list
    return sum_list, avg_list, len_list

# main code
test_list = [1,64,71,-3]
test_sum, test_avg, test_len = num_list_stats(test_list) # call function and bind return tuple
```

If you aren't convinced then try this piece of code.

```python
def tuple_test(x,y):
    return x, y

print(tuple_test(1,2))          # prints (1,2)
print(type(tuple_test(1,2)))    # prints <class 'tuple'>
```

### 3.2. Zipping Two Tuples

Zipping tuples together is a very useful thing to do when we want to combine tuples together and loop over them.

The zip operation is demonstrated by the following code snippet. Note both must be the same length.

```python
tuple_one = (1,2,3)
tuple_two = ("a","b","c")

for x,y in zip(tuple_one, tuple_two):
    print(x,y)

# prints
# 1 a
# 2 b
# 3 c
```

You can also zip a tuple and list.

```python
tuple_one = (1,2,3)
list_one = ["a","b","c"]

for x,y in zip(tuple_one, list_one):
    print(x,y)

# prints
# 1 a
# 2 b
# 3 c
```

## 4. Tuple Methods

| Method | Description |
--- | ---|
| ``count()``	| Returns the number of times a specified value occurs in a tuple |
| ``index()`` |	Searches the tuple for a specified value and returns the position of where it was found |

[W3Schools - Tuple Methods](https://www.w3schools.com/python/python_ref_tuple.asp)

## 5. What if I Need to Change a Tuple?

You can do this by converting (casting) the ``tuple`` to a ``list`` using the ``list()``  and ``tuple()`` functions.

```python
car_tuple = ("Audi", "Mercedes", "Ferrari")
temp = list(car_tuple)   # create a tempory copy of the tuple as a list
temp[0] = "Ford"         # Overwrite the 1st item 
car_tuple = tuple(temp)  # Reassign car_tuple as a new tuple using temp
print(car_tuple) # prints ("Ford", "Mercedes", "Ferrari")
```

*** 
# === TASK ===
In **main.py** there is a function called ``tuple_search()`` that you need to update.

The function should count the number of times an item occurs in the tuple and the index (position) of the first of these occurences.

``tuple_search(t, search_item)``

For example,

```python
spaghetti_soup = ("a", "b", "g", "c", "a", "z", "g", "a", "g", "y")
tuple_search(spaghetti_soup, "g")
```
Should return ``(3, 2)``

Copy and paste the following into **main.py** to get started.
```python
def tuple_search(t, search_index):
    pass

if __name__ == "__main__":
    # main code
    spaghetti_soup = ("a", "b", "g", "c", "a", "z", "g", "a", "g", "y")
    print(tuple_search(spaghetti_soup, "g")) # should print (3, 2)
```
***

# References 

[Python Tuple Methods - W3schools](https://www.w3schools.com/python/python_tuples_methods.asp)