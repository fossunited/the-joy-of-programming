# Lists

In this lesson we are going to see how to represent a list of values
in Python.

A list of values is written in the following format.

```{.python .joy .example}
numbers = [1, 2, 3, 4, 5]
print(numbers)
```

We could even have a list of names.

```{.python .joy .example}
names = ["Alice", "Bob", "Charlie"]
print(names)
```

You may be wondering why the output has single quotes around the names
while we have given double quotes. Python doesn't distinguish between double
quotes or single quotes. The output is going to be the same irrespective of
the kind of quotes you've used.

We could also create a list by using the values of existing variables.

```{.python .joy .example}
a = "Alice"
b = "Bob"
c = "Charlie
names = [a, b, c]
print(names)
```

## Length of a list

Python has a built-in function `len` to find the length of a list.

```{.python .joy .example}
numbers = [1, 2, 3, 4, 5]
print("we have", len(numbers), "numbers")
```

## Accessing Elements

The elements of a list can be accessed using the `[]` operator.

```{.python .joy .example}
names = ["A", "B", "C", "D"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
```

The index of a list starts from `0` and going up to `n-1`, where `n` is
the length of the list.

In the previous example, `names[0]` gives the first element the
list and `names[3]` gives the last element as the length of the list is `4`.

Guess what would be the output of this program?

```{.python .joy .example}
numbers = [5, 4, 3, 2]

x = numbers[1] + numbers[2]
print(x)
```
