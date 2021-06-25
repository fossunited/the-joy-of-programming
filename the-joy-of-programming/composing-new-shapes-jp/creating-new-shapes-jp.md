# Creating New Shapes

So far, we are only able to draw the primitive shapes that are already
available in the system. We've drawn new shapes like donut, eye etc
by combining simple shapes. While that was fun, it would quickly become
cumbersome if we try to draw these shapes multiple times.

Wouldn't it be nice if we can explain to computer how to draw a new
shape and it rememebers it forever? In this lesson we are going to see
how to use functions to achieve exactly this!

## Functions

We've already seen how to use functions. The `print`, `show` and even
`circle`, `rectangle` etc. are some already available functions that we
used.

Let's review the syntax of calling functions.

```{.python .joy .example}
print(1, 2, 3)

shape = circle(r=50)
show(shape)
```

Function are called by passing inputs to it, called arguments. Some
functions take a single aregument, some take more than one and some
don't take any arguments at all.

The arguments to a function can be passed either by position (`show(shape)`)
or by name (`circle(r=50)`). Some functions accept arguments only
by name. We'll learn more about that in the latter lessons.

## Creating Functions

We can create our own functions. Once we create a new function, it can be
used just like the built-in functions.

Lets start with creating a function `dot` to create a dot at specified position.

```{.python .joy .example}
def dot(x, y):
    c = circle(x=x, y=y, r=5, fill="black")
    return c

c = circle(r=50)
d = dot(x=0, y=50)
show(c, d)
```

There are two parts to the program in the above example. The first is
defining the function `dot` and the second part is calling that function
to create a dot shape and show it.

Let's understand the second part first. We've created a circle and placed
a dot at the top-most point of the circle.

Now, let's look at how the function `dot` is defined.

```
# define a function dot that takes two arguments with names x and y
def dot(x, y):
    # create a circle filled with black, having center (x,y) and radius 5
    c = circle(x=x, y=y, r=5, fill="black")

    # return the shape c to whover calls this function
    return c
```

The first line specified the function name and the names of the arguments
followed by the body of the function. Each line in the body of the function
starts with four spaces, called indentation. Python uses indentation to
identify which lines are part of the function and which are outside.

!!! Keywords

    Every programming language has some special words reserved to be used
    only in some particular ways. The keywords can not be used as names of
    variables or functions.

    The `def` and `return` are the keywords that we've used in the above
    example. There are many more keywords in Python and you can find a list
    of them in the [Python documentation][1].

    [1]: https://docs.python.org/3/reference/lexical_analysis.html#keywords

{{ Exercise("reddot-jp") }}
{{ Exercise("square-jp") }}
{{ Exercise("donut-func-jp") }}

{{ Exercise("concentric-circles-x3-jp") }}
{{ Exercise("concentric-circles-x3-growing-jp") }}

