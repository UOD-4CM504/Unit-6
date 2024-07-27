# Sets  

We will not spend long on sets as their use is somewhat limited, but they can come in very handy at times.

1. Unordered and unindexed
2. Items are immutable (unchangeable)
3. Set is mutable (changable)
4. Collection of distinct items

By **unordered and unindexed** we mean that the set does not have an order and therefore does not use indexing. You cannot access an item in a set by an index.

By **items are immutable** we mean that you cannot change an item in the set, this follows from it being **unordered and unindexed**. If you can't access an item, you definitely can't change it.

By **set is mutable** we mean that you can add and remove items from the set.

By **collection of distinct items** we mean that a set cannot contain duplicates.

You define a set as follows.

```python
car_set = {"Audi", "Porsche", "Ford"}
```

Note that if you try and define a set with multiple items, it will only include one copy of each distinct item.

```python
car_set = {"Audi", "Porsche", "Ford", "Audi"} # set is {"Audi", "Porsche", "Ford"}
```

## 1. Set Items
There are a few things we can do to a set involving items.
### 1.1 Is an Item in the Set?
The ``in`` keyword checks whether an item is in a given set and returns ``True`` or ``False``.

```python
"Audi" in car_set  # evaluates to True
"Skoda" in car_set # evaluates to False
```

Note that ``in`` can also  be used on lists and tuples.

```python
car_list = ["Audi", "Porsche", "Ford", "Audi"]
car_tuple = ("Audi", "Porsche", "Ford", "Audi")
"Audi" in car_list  # evaluates to True
"Audi" in car_tuple  # evaluates to True
```

### 1.2 Add an Item

You can add an item to a set by using the ``add()`` method.

```python
car_set. add("Skoda") # set is {"Audi", "Porsche", "Ford", "Skoda"}
```

### 1.3 Remove an Item

You can remove an item in a set by using the ``remove()`` method.

```python
car_set. remove("Ford") # set is {"Audi", "Porsche", "Skoda"}
```

## 2. Looping Through a Set

Just like lists and tuples, you can loop through a set.

```python
car_set = {"Audi", "Porsche", "Ford"}
for car in car_set:
  print(car)

# prints...
# Audi
# Porsche
# Ford
```

## 3. Joining Sets

You can join sets using either the ``union()`` or ``intersection()`` methods.

For a mathematician, this is a very loose definition, but basically the ``union()`` method will include all the items that are in both sets, but not any duplicates.

```python
a = {1,2,3}
b = {1,4,5,6}
c = a.union(b) # c now contains {1,2,3,4,5,6}
```

The intersection includes only the items that appear in both sets.

```python
a = {1,2,3}
b = {1,4,5,6}
c = a.intersection(b) # c now contains {1}
```

## 4. Set Methods

There are a number of set methods that you can use, we have seen two in ``add()`` and ``remove()``. We will not look at these in detail in this course.

You can find a full list here [Python Set Methods - W3schools](https://www.w3schools.com/python/python_sets_methods.asp).

I suggest you use these when you are studying sets in computational mathematics.

***
# === TASK ===
Copy the following into **main.py**.
```python
def items_in_both(a,b):
    pass

if __name__ == "__main__":
    # main
    # use this code to help check the function
    a = {1,2,3}
    b = {1,4,5,6}
    print(items_in_both(a,b))    # prints {1}
```
Update the function ``items_in_both()`` so that it returns the set that contains only the items that appear in both sets.
***

# References

[Python Sets - W3schools](https://www.w3schools.com/python/python_sets.asp)