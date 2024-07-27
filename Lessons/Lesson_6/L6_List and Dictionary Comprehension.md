# List/Dictionary Comprehension

List and dictionary comprehension is an incredibly powerful technique for writing compact code. It basically allows you to generate complicated lists or dictionaries in one line of code.

List and dictionary comprehension is something that takes time to get used to and I think the easiest way to understand it is to see it in action.

In this lesson you will see simple code snippets and then see the same code rewritten using list/dictionary comprehension. 

You should note how compact this code looks, but how as the complexity builds up it can be harder to read.

**I suggest that you copy the code into [Python Tutor](https://pythontutor.com/) to make sure you understand it**.

## 1. List Comprehension

We will start with the example given on [W3schools](https://www.w3schools.com/python/python_lists_comprehension.asp).

```python
# filter list for words with "a" in.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) # prints ['apple', 'banana', 'mango']
```
We can rewrite this using list comprehension.

```python
# using list comprehension
# filter list for words with "a" in.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # prints ['apple', 'banana', 'mango']
```

Notice that list comprehension is in the following form.

```python
[<expression> for <item> in <iterable> if <condition> == True]
```
The return value is a new list, leaving the old list unchanged.

### 1.1 Even Numbers
The following is a simple program that generates the even numbers between 1 and 100.
```python
# generate even numbers between 1 and 100
even_num_list = []
for x in range(1,51):
    even_num_list.append(2*x)

print(even_num_list) # prints [2,4,6, ...,98,100]
```

We can rewrite this using list comprehension.

```python
# using list comprehension
# generate even numbers between 1 and 100
even_num_list = [2*x for x in range(1,51)]
print(even_num_list) # prints [2,4,6, ...,98,100]
```

Here we didn't use a condition so our list comprehension was in the form.

```python
[<expression> for <item> in <iterable>]
```

An alternative program that generates the even numbers uses the ``%`` modulus operator.

```python
# generate even numbers between 1 and 100
even_num_list = []
for x in range(1,101):
    if x % 2 == 0:
        even_num_list.append(x)

print(even_num_list) # prints [2,4,6, ...,98,100]
```
We can rewrite this using list comprehension.

```python
# using list comprehension
# generate even numbers between 1 and 100
even_num_list = [x for x in range(1,101) if x % 2 == 0]
print(even_num_list) # prints [2,4,6, ...,98,100]
```

Here we did use a condition so our list comprehension was in the form.

```python
[<expression> for <item> in <iterable> if <condition> == True]
```

### 1.2 Length of Words

The following program takes a list of words and then calculates the length of each of the words.
```python
# compute the length of each word in the list
words = ["Python", "is", "a", "cool", "programming", "language"]
len_words = []
for w in words:
    len_words.append(len(w))

print(len_words) # prints [6, 2, 1, 4, 11, 8]
```

We can rewrite this using list comprehension.

```python
# using list comprehension
# compute the length of each word in the list
words = ["Python", "is", "a", "cool", "programming", "language"]
len_words = [len(s) for s in words]
print(len_words) # prints [6, 2, 1, 4, 11, 8]
```

We can also take a sentence and use the ``split()`` method to generate a list of words from a string and then do the above.

```python
# compute the length of each word in the sentence
text = "Python is a cool programming language"
len_words = []
for w in text.split(" "):    
    len_words.append(len(w))

print(len_words) # prints [6, 2, 1, 4, 11, 8]
```

We can rewrite this using list comprehension.

```python
# using list comprehension
# compute the length of each word in the sentence
text = "Python is a cool programming language"
len_words = [len(s) for s in text.split(" ")]
print(len_words) # prints [6, 2, 1, 4, 11, 8]
```


## 2. Nested List Comprehension

What about nested ``for`` loops? List comprehension has you covered.

### 2.1 Length of Words in a List of Sentences
This is a program that takes a list of sentences and creates a list containing the length of each word in each sentence.

```python
# compute the length of each word in a list of sentences
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
len_words = []
for sentence in sentence_list:
    for word in sentence.split(" "):
        len_words.append(len(word))

print(len_words) # prints [6, 2, 1, 4, 11, 8, 1, 4, 2, 7, 11, 2, 2, 4]
```

We can rewrite this using list comprehension.

```python
# using list comprehension
# compute the length of each word in a list of sentences
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
len_words = [len(word) for sentence in sentence_list for word in sentence.split(" ")]
print(len_words) # prints [6, 2, 1, 4, 11, 8, 1, 4, 2, 7, 11, 2, 2, 4]
```
Which is in the form:
```python
[<expression> for <inner_list> in <outer_list> for <item> in <inner_list>]
```

The output produced a single list with the length of the words. 

What if we want the list to contain a separate list of word lengths for each of the sentences? e.g. ``[[6, 2, 1, 4, 11, 8], [1, 4, 2, 7], [11, 2, 2, 4]]``

```python
# compute the length of each word in a each of the sentences
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
len_words = []
for sentence in sentence_list:
    temp = []
    for word in sentence.split(" "):
        temp.append(len(word))
    len_words.append(temp)

print(len_words) # prints [[6, 2, 1, 4, 11, 8], [1, 4, 2, 7], [11, 2, 2, 4]]
```

We can rewrite this using list comprehension.

```python
# using list comprehension
# compute the length of each word in each of the sentences
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
len_words = [[len(word) for word in sentence.split(" ")] for sentence in sentence_list]
print(len_words) # prints [[6, 2, 1, 4, 11, 8], [1, 4, 2, 7], [11, 2, 2, 4]]
```

Which is in the form:
```python
[[<expression> for <item> in <inner_list>] for <inner_list> in <outer_list> if <condition> == True]
```
That is, produce a list from each of the inner lists of the outer list.

### 2.2 Nested with a Condition

What about adding a condition so that we only store the length of the words that are less than 4.

```python
# compute the length of each word less than 4 in a list of sentences
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
less_than_4 = []
for sentence in sentence_list:
    for word in sentence.split(" "):
        if(len(word) < 4):
            less_than_4.append(len(word))

print(less_than_4) # prints [2, 1, 1, 2, 2, 2]
```

We can rewrite this using list comprehension.

```python
# using list comprehension
# compute the length of each word less than 4 in a list of sentences
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
less_than_4 = [len(word) for sentence in sentence_list for word in sentence.split(" ") if len(word) < 4]
print(less_than_4) # prints [2, 1, 1, 2, 2, 2]
```
## 3. Dictionary Comprehension

We can also do comprehension using dictionaries.

Consider the following example:

```python
# compute the length of each word in the list and store it with the word
words = ["Python", "is", "a", "cool", "programming", "language"]
len_words = {}
for s in words:
    len_words[s] = len(s)
    
print(len_words) # prints {'Python': 6, 'is': 2, 'a': 1, 'cool': 4, 'programming': 11, 'language': 8}
```

We can write this using dictionary comprehension as follows:

```python
# compute the length of each word in the list and store it with the word
words = ["Python", "is", "a", "cool", "programming", "language"]
len_words = {s:len(s) for s in words}
print(len_words) # prints {'Python': 6, 'is': 2, 'a': 1, 'cool': 4, 'programming': 11, 'language': 8}
```
Here for each ``s`` in the list ``words`` we store the key:value pair ``s:len(s)``

The general form is:
```python
{<key>:<value> for <item> in <iterable> if <condition> == True}
```
The ``return`` value is a new dictionary, leaving the list we used to generate the dictionary unchanged.

We could also change this to just store the words that are less than length 4.
```python
# compute the length of each word in the list and store it with the word
words = ["Python", "is", "a", "cool", "programming", "language"]
less_than_four = {s:len(s) for s in words if len(s) < 4}
print(less_than_four) # prints {'is': 2, 'a': 1}
```

## 4. Nested Dictionary Comprehension

What about nested for loops? Dictionary comprehension also has you covered.

```python
# compute the length of each word in the list of sentences and store it with the word
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
len_words = {}
for sentence in sentence_list:
    for word in sentence.split(" "):
        len_words[word] = len(word)

print(len_words)
# prints {'Python': 6, 'is': 2, 'a': 1, 'cool': 4, 'programming': 11, 'language': 8, 'I': 1, 'love': 4, 'to': 2, 'program': 7, 'Programming': 11, 'so': 2}
```

We can rewrite this using dictionary comprehension.

```python
# using dictionary comprehension
# compute the length of each word in the list of sentences and store it with the word
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
len_words = {word:len(word) for sentence in sentence_list for word in sentence.split(" ")}
print(len_words) 
# prints {'Python': 6, 'is': 2, 'a': 1, 'cool': 4, 'programming': 11, 'language': 8, 'I': 1, 'love': 4, 'to': 2, 'program': 7, 'Programming': 11, 'so': 2}
```

Which is in the form:
```python
newlist = {<key>:<value> for <inner_list> in <outer_list> for <item> in <inner_list>}
```
We could also compute the length of each word in the sentences that is less than 4.
```python
# compute the length of each word in the list of sentences that is less that 4 and store it with the word
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
less_than_4 = {}
for sentence in sentence_list:
    for word in sentence.split(" "):
        if len(word) < 4:
            less_than_4[word] = len(word)

print(less_than_4) # prints {'is': 2, 'a': 1, 'I': 1, 'to': 2, 'so': 2}
```
We can rewrite this using dictionary comprehension.

```python
# using dictionary comprehension
# compute the length of each word in the list of sentences that is less that 4 and store it with the word
sentence_list = ["Python is a cool programming language", "I love to program", "Programming is so cool"]
less_than_4 = {word:len(word) for sentence in sentence_list for word in sentence.split(" ") if len(word) < 4}
print(less_than_4) # prints {'is': 2, 'a': 1, 'I': 1, 'to': 2, 'so': 2}
```

Which is in the form:
```python
newlist = {<key>:<value> for <inner_list> in <outer_list> for <item> if <condition> == True}
```

## 5. Comprehension on Dictionaries

Note that you can do comprehension using any iterable such as a ``range``, ``list`` or ``dict``.

### 5.1 Range

We already saw this at the start with the even numbers.

```python
# using list comprehension
# generate even numbers between 1 and 100
even_no_list = [x for x in range(1,101) if x % 2 == 0]
print(even_no_list)
```

### 5.2 Dictionary

We could get the list of student names from a dictionary of students.

```python
student_dict = {
    1123425: "Ada Lovelace",
    1425243: "Katherine Johnson",
    1512414: "Alan Turing"
}

student_names = [value for key, value in student_dict.items()]
print(student_names) # prints ['Ada Lovelace', 'Katherine Johnson', 'Alan Turing']
```

Note we could just get this using ``student_dict.values()``.

The following takes a dictionary of students and adds their email address to their data. 

```python
# automatically generate student emails and store them in a nested dictionary.
def email_from_name(name):
    [first_name, surname] = name.split(" ")
    return f"{first_name[0]}.{surname}.unimail.derby.ac.uk"

student_dict = {
    1123425: "Ada Lovelace",
    1425243: "Katherine Johnson",
    1512414: "Alan Turing"
}

student_info_dict = {key:{"Name":value, "Email":email_from_name(value)} for key, value in student_dict.items()}
print(student_info_dict) 
# prints {1123425: {'Name': 'Ada Lovelace', 'Email': 'A.Lovelace.unimail.derby.ac.uk'}, 1425243: {'Name': 'Katherine Johnson', 'Email': 'K.Johnson.unimail.derby.ac.uk'}, 1512414: {'Name': 'Alan Turing', 'Email': 'A.Turing.unimail.derby.ac.uk'}}
```

***
# === TASK ===

Use list comprehension to find the sum of all numbers that are divisable by ``3`` between ``1`` and an upper limit ``n``. If you are struggling, write this in a more "traditional" format first and then convert it to list comprehension.

You should update the function ``sum_div_3(n)`` so that it returns the correct sum.

For example, ``sum_div_3(12)`` should sum up ``3,6,9`` and ``12`` which totals to ``30``.

Copy and paste the following into **main.py**.
```python
def sum_div_3(n):
    """you should update div_by_3_list to generate the list of numbers divisible by 3 and return their sum.

    e.g. for n = 10 it should look at 1,2,3,4,5,6,7,8,9,10 and the list should contain [3,6,9]. The function should then return the sum of this list, in this case 18"""
    div_by_3_list = []
    return sum(div_by_3_list)


if __name__ == "__main__":
    print(sum_div_3(10))  # should print 18
    print(sum_div_3(12))  # should print 30
    print(sum_div_3(100))  # should print 1683

```
***