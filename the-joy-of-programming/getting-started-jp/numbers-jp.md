# Numbers

It is very easy to work with numbers in Python. You can in fact use
Python as a pretty good calculator.

## Printing Numbers

Let's write a program to print the number 4.

```{.python .joy .example}
print(4)
```

Try changing the number 4 to some other number and run the program.

## Arithmetic Expressions

Python supports usual arithmetic operations `+`, `-`, `*` and `/` for addition, subtraction, multiplication and division respectively. Please note the multiplication operator is `*`, called an asterisk or a star.

Let us try doing some simple computations using these operators.

```{.python .joy .example}
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
```

As you can see the result of `7/2` is decimal number `3.5`. Python knows
how to handle various types of data, but for now we will just stick to
numbers, both integers and decimal numbers.

It is also possible to combine multiple expressions. Look at the following
example. Will it print `27` or `13`?

```{.python .joy .example}
print(7 + 2 * 3)
```

That prints `13` because multiplication and division are done before addition
and subtraction.

If we really need `7+2` multiplied by `3`, we need to keep `7+2` in parathesis or brackets.

```{.python .joy .example}
print((7 + 2) * 3)
```

## Big Numbers

Python is pretty good at handling big numbers. Can you guess what would the output of the following computation?

```{.python .joy .example}
print(111111111 * 111111111)
```

Python also has an exponential operator `**`. If you want to compute the value of `2`<sup>`10`</sup>, you need to write it as `2 ** 10` in Python.

```{.python .joy .example}
print(2 ** 10)
```

Why stop at `2`<sup>`10`</sup>? How about `2`<sup>`100`</sup>?

```{.python .joy .example}
print(2 ** 100)
```

Is that a big number? Not really! Try to compute `2`<sup>`1000`</sup> and
see the result.

```{.python .joy .example}
print(2 ** 1000)
```

Computers are really good at doing a lot of computations. We just need
to learn how to tell them what to do.

{{ Exercise("five-factorial-jp") }}
