# The Elements of Programming

A programming languge is more than just giving intructions to the computer. It is also a framework to organize our ideas to achieve something bigger.

## The `print` function

In programming, we ofen need to display the value of some computation. In Python, the `print` function is used to display value of something.

When you run the following code, it would display the number 45 in the output area. Try out and see.

```
print(45)
```

You can print multiple things, one in each line.

```
print(1)
print(2)
print(3)
print(4)
print(5)
```

You could also print more than one thing at a time.

```
print(1)
print(1, 2)
print(1, 2, 3)
```

Printing numbers alone is not so much fun. Would it be fun to compute something big and see?

## Simple Arthemetic Operations

Python supports usual arthemetic operations `+`, `-`, `*` and `/` for addition, subtraction, multiplication and division respectively. Please note the the multiplcaition operator is `*`, called an asterisk or a star.

Let us try doing some simple computations using these operators.

```
print(7+2)
print(7-2)
print(7*2)
print(7/2)
```

As you can see the result of `7/2` is decimal number `3.5`. Python know how to handle various types of data, but for now we will just stick to numbers, both integers and decimal numbers.

Python is pretty good at handling big numbers. Can you guess what would the output of the following computation?

```
print(111111111 * 111111111)
```

Python also has an exponential operator `**`. If you want to compute things like 2<sup>10</sup> etc, you need to compute it as `2 ** 10` in Python.

```
print(2 ** 10)
```

Why stop at 2<sup>10</sup>? How about 2<sup>1000</sup>?

```
print(2 ** 1000)
```

That is a pretty big number. Isn't it?

Computers are really good at doing lot of computations. We can just need to learn how to tell them what to do.

## Variables

We are really bad at keeping track of so many numbers. We like to name everything. In the context of programming we use variables to give a name to some value.

For example, the following program using the values of variables `w` and `h` to compute the value of variable `area`.

```
w = 20
h = 10
area = w * h
print(area)
```

Consider the following piece of code. It is drawing a circle at `(100, 100)` with diameter `100`.

```
circle(100, 100, 100)
```

 Which `100` would you change to make the circle smaller? Isn't that a bit confusing to manage the number 100 at three different places? See what happens if we give names to these values.

```
x = 100
y = 100
d = 100

circle(x, y, d)
```

 Now the program is lot of clear and easy to understand. Using appropriate variable names gives a lot of clarity to our programs.

Let us look at another example. This programs draws a donut, a small circle inside another bigger circle.

```
circle(100, 100, 100)
circle(100, 100, 50)
```

Let's say we want to make the donut bigger. We may have to increase the diameter of both of these circles. And it is important to maintain the same proportions so that the new figure looks similar to the old one.

Let's try rewriting that above program using variables.

```
x = 100
y = 100
d = 100

circle(x, y, d)
# the smaller circle will be half the size of the bigger circle
circle(x, y, d/2)
```

As you can see, the program captured the essense that the size of the smaller circle is half of the size of the bigger circle. You can change the value of `d` to any number that you want, the entire donut would change it's size which retaining the shape. You could also try to change `x` or `y` to move the donut to a different place.


### Exercise: Two Circles in a Row with variables

Draw two circles in a row, but this time using variables.

If your program is correct, you should be able to change the value of x or y to
change the position of the drawing and d to change the size of the drawing while retaining the shape.

```
x = 100
y = 100
d = 75

circle(x, y, d)
# draw the second circle
```

## Modifying Variables

The value of a variable can changed too.

```
x = 100
y = 100
d = 100
circle(x, y, d)

# move right by 20 units and draw another circle
x = x+20
circle(x, y, d)

# do the previous step again
x = x+20
circle(x, y, d)
```

## Functions

While variables makes the code a lot easier to understand there is still a problem of doing the same thing multiple times.

Suppose we wnat to draw two donuts of different sizes. How would you do it. Straight forward way is to


We could write this program simply as: