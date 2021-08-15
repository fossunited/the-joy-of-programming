# The For Loop

Suppose you have to do a task a hundred times in your program. Wouldn't it be too cumbersome to duplicate that code 100 times?

Every programming language will have a way to repeat things. In Python, it is done using a for loop.

## The For Loop

We use a `for` loop in Python to _iterate_ over a list of values.

```{.python .joy .example}
numbers = [10, 20, 30]
for n in numbers:
    print(n)
print("done")
```

The `for` loop goes over each value in the list `numbers` and executes
the body of the loop for every value of `n`.

Please note that the code that is part of the loop is indented (moved
to the right by adding spaces at the beginning of the line). Just like
writing a function, when writing a for loop, the code that is part of
the loop is identified by the indentation.

You can understand that the line `print(n)`  is part of the loop, but
the line `print("done")` is outside the loop.

Let's try to iterate over a list of names.

```{.python .joy .example}
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello", name)
```

## The `range`

The `range` function gives a sequence of numbers. It is handy when we
want to iterate a fixed number of times.

```{.python .joy .example}
for i in range(5):
    print(i)
```

The function `range(5)` gives a sequence of numbers 0, 1, 2, 3 and 4. Since
we are printing the value of `i` in the body, we will see that the numbers
0, 1, 2, 3 and 4 get printed.

Notice that when you call `range(n)`, it gives numbers from `0`, `1`,..., `n-1`. The number `n` is not included in them.

We can also specify the starting number by specifying two arguments to `range`.

```{.python .joy .example}
for i in range(2, 5):
    print(i)
```

The funciton `range(a, b)` gives numbers from `a`, `a+1`,..., `b-1`.

## Looping Patterns

We've seen how to use a for loop, but let's review various looping
patterns to get a sense of how loops are used in different scenarios.
Some of these we have already seen above.

### Iterate over a list of values

The for loop can be used to loop over a list of values and perform a
task for every line of code

```{.python .joy .example}
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello", name)
```

### Repeat something n times

The for loop can be used to do the exact same task multiple times. The
following example prints `Hello!` five times.

```{.python .joy .example}
for i in range(5):
    print("Hello!")
```

### Updating a variable in every iteration

The following example prints five numbers starting from 10 to 50, incrementing
the current number by 10 in each iteration.

```{.python .joy .example}
n = 10
for i in range(5):
    print(n)
    n = n + 10
```

The line `n = n + 10` may look a little strange if you have never seen
something like that before. It just means that, take the current value
of `n`, add 10 to it and assign it back to variable `n`. So, that line
of code increments the value of n by 10.

Initializing a variable before the loop and updating it in every iteration
of the loop is one of the common patterns used with loops.

### Using the loop variable to compute values

The previous example of printing numbers from 50 to 100 can also be
achieved in the following way.

```{.python .joy .example}

for i in range(5):
    n = 10 + i * 10
    print(n)
```

## Exercises

{{ Exercise("countdown-jp") }}
{{ Exercise("powers-of-two-jp") }}
