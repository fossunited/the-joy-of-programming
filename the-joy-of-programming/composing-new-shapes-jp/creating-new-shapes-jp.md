# Creating New Shapes

So far, we are only able to draw the primitive shapes that are already
available in the system. We've drawn compute shapes like donut, eye etc
by combining simple shapes. While that was fun, it would quickly become
cumbersome if we try to draw these shapes multiple times.

Wouldn't it be nice if we can explain to computer how to draw a compound
shape and it rememebers it forever? In this lesson we are going to see
how to use functions to achieve exactly this!

## Functions

We've seen already how to use functions. The `print`, `show` and even
`Circle`, `Rectangle` etc. are some already available functions that we
used.

Let's look at the syntax of calling functions.

```{.python .joy .example}
print(1, 2, 3)

shape = Circle(radius=50)
show(shape)
```

Function are called by passing inputs to it, called arguments. Some
functions take a single aregument, some take more than one and some
don't take any arguments at all.

The arguments to a function can be passed either by position (`show(shape)`)
or by name (`Circle(radius=50)`). Some functions accept arguments only
by name. We'll learn more about that in the latter lessons.

## Creating Functions

The `def` statement is used to create functions. A function would
take some inputs, called arguments, and return a value back. There are
functions (like `print` and `show`) which don't return a value as well.

Let's look at creating a function to create a donut.

```{.python .joy .example}
def donut(r):
    shape = Circle(radius=r) + Circle(radius=r/2)
    return shape

shape = donut(100)
show(shape)
```

In the above example. we've created a donut by calling `donut(100)`. That
executes the body of the function after setting the value of variable `r`
to the first argument passed to the function.

We could extand the above `donut` function to also take center as an
argument so that we can draw it wherever we want.

```{.python .joy .example}
def donut(center, radius):
    c1 = Circle(center=center, radius=radius)
    c2 = Circle(center=center, radius=radius/2)
    return c1+c2

r = 50
d1 = donut(Point(x=-r, y=0), r)
d2 = donut(Point(x=r, y=0), r)
show(d1, d2)
```

The `donut` function now takes two arguments `center` and `radius`. It
may be confusing to see `center=center` and `radius=radius` in the body
of the function. That left hand side of the `=` is the name of the argument
and the right hand side is the value that we are passing.

As you can see, we've used the donut function twice to draw two donuts,
one on the left side of the origin and another on the right.
