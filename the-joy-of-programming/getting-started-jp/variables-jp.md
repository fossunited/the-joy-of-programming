# Variables

Instead of remembering all the values that we are interested to work with,
we can give it a name let the computer remember it.

```{.python .joy .example}
x = 5
y = 2
print(x+y)
```

In the above program, `x` and `y` are variables holding values `5` and `2`
respectively.

The variables can take any type of value. In the following example, the
variable `name` holds a value of type string.

```{.python .joy .example}
name = "Joy"
print(name)
```

Notice the difference between using a variable and a string. Notice the
difference by observing the output of the following program.

```{.python .joy .example}
name = "Joy"

print("name")
print(name)
```

## Updating value of variables

It is very common to update the value of a variable as part of a
program.

```{.python .joy .example}
x = 5
x = x + 1
print(x)
```

In the above example, the variable x starts with value 5 and it gets
incremented in the second line.

When you see code like `x = x + 1`, it may look very confusing in the
beginning, but all it means is that compute the expression on the right
hand side and assign it to the variable in the left hand side.

It will compute the value of `x + 1` first, which will be `6` and assigns
that to variable `x`. The variable `x` will have a value `6` after that.

## Multiple Assignments

Python allows assigning multiple values to multiple variables in a single
statement. It is very handy to assign values for related variables at once.

```{.python .joy .example}
x, y = 100, 200
print(x)
print(y)
```

## Printing

Printing values of the variables during the execution of a program is v
very common way to understand how the program is working and identify any
defects.

The `print` function supports printing multiple values at once.

```{.python .joy .example}
print("hello", "world!")
print(1, 2, 3)
```

This could be used to generate meaningful messages like the following:

```{.python .joy .example}
mango_price = 45
mango_quantity = 5

print("We have purchased", mango_quantity, "mangoes.")
print("The price of each mango is", mango_price, "rupees.")

total_price = mango_price * mango_price
print("The total price is", total_price, "rupees.")
```

